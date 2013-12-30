import pygame
import Gui_Screen
import Gui_Client
from Data_CONST import *

# ==============================================================================
class Gui_FleetScreen(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    i_view_size  = 20
    i_list_start = 0
    i_list_size  = 0
# ------------------------------------------------------------------------------
    def __init__(self):
        super(Gui_FleetScreen,self).__init__()
        self.i_num_fleets  = 0
        self.i_fleet_shown = -1
# ------------------------------------------------------------------------------
    def reset_triggers_list(self):
        super(Gui_FleetScreen,self).reset_triggers_list()
        self.add_trigger({'action': "ESCAPE",                       'rect': pygame.Rect((558, 432), (65, 25))})
        self.add_trigger({'action': "screen", "screen": "leaders",  'rect': pygame.Rect((553, 385), (70, 20))})
        self.add_trigger({'action': "SELECT_ALL",                   'rect': pygame.Rect((353, 385), (70, 20))})
        self.add_trigger({'action': "RELOCATE",                     'rect': pygame.Rect((445, 385), (85, 20))})
        self.add_trigger({'action': "SCRAP",                        'rect': pygame.Rect((553, 385), (70, 20))})
        self.add_trigger({'action': "filter", "filter": "support",  'rect': pygame.Rect((424, 432), (60, 20))})
        self.add_trigger({'action': "filter", "filter": "combat",   'rect': pygame.Rect((485, 432), (60, 20))})
        self.add_trigger({'action': "NEXT_FLEET",                   'rect': pygame.Rect((287, 250), (25, 18))})
        self.add_trigger({'action': "PREVIOUS_FLEET",               'rect': pygame.Rect((22, 250),  (25, 18))})
        self.add_trigger({'action': "SCROLL_UP",                    'rect': pygame.Rect((605, 61),  (15, 25))})
        self.add_trigger({'action': "SCROLL_DOWN",                  'rect': pygame.Rect((605, 327), (15, 25))})
# ------------------------------------------------------------------------------
    def get_fleets(self, ships):
        """should return a list of lists of ships that are sorted by their location"""
        ships.sort(key=lambda ship: ship.get_destination())
        fleets = [[]]
        num_fleets = 0
        dest_pos = (ships[0].i_dest_star_id , ships[0].i_x, ships[0].i_y)
        for ship in ships:
            ship_tup = (ship.i_dest_star_id, ship.i_x, ship.i_y)
            if ship_tup == dest_pos:
                fleets[num_fleets].append(ship)
            else:
                fleets.append([])
                num_fleets += 1
                fleets[num_fleets].append(ship)
                dest_pos = (ship.i_dest_star_id, ship.i_x, ship.i_y)
        return fleets
# ------------------------------------------------------------------------------
    def palette_test(self):
        for i in range(17):
            print("test disp%d x:%d y:%d"%(i,0,i))
            self.draw_image_by_key((120,25*i), 'SHIP', 0, i+17)
# ------------------------------------------------------------------------------
    def draw(self):
        players_ships = self.list_ships(self.get_player_id())
        ship_square_x = 60 #guess of the size of the ship displayed
        ship_square_y = 60

        #print("Player %d has %d ships" % (self.get_player_id(), len(players_ships)))
        #for ship in players_ships:
        #    if ship.exists():
        #        print("->name :%s %d" % (ship.get_design()['name'], ship.get_owner()))

        self.draw_image_by_key((0, 0), 'Fleet_screen.panel')

        self.palette_test()

        if len(players_ships) > 0:
            fleets = self.get_fleets(players_ships);
            self.i_num_fleets = len(fleets)
            if self.i_fleet_shown == -1:
                current_fleet = fleets[0]
                self.i_fleet_shown = 0
            elif self.i_fleet_shown not in range(len(fleets)):
                current_fleet = fleets[0]
            else:
                current_fleet = fleets[self.i_fleet_shown]

            current_fleet.sort(key = lambda ship: ship.get_design()['size'], reverse = True)
            for i in xrange(len(current_fleet)):
                ship = current_fleet[i];

                #no scrolling, just 20 ships shown, 5 rows of 4 ships
                column = i % 4 # column 0..4
                row = (i - i % 4) / 4 # row 0..5

                #here we'll add a trigger for each ship shown
                image_position = (345 + column * ship_square_x, 55 + row * ship_square_y)
                self.add_trigger({'action': "ship_info", 'ship': ship, 'rect': pygame.Rect(image_position, (ship_square_x, ship_square_y))})

                if ship.has_no_image():
                    ship.determine_image_keys(self.get_me().i_color)
                keys = ship.get_image_keys()
                print("displaying ship %d %d dest %d x:%d y:%d"%(keys[0],keys[1],ship.get_destination(),ship.get_x(),ship.get_y()))
                self.draw_image_by_key(image_position, 'SHIP', keys[0], keys[1])
# ------------------------------------------------------------------------------
    def display_ship_info(self, ship):
        """Displays ship information text on fleet screen """

        self.draw() ##redraws the screen, to erase previous text

        design        = ship.get_design()
        weapons       = design['weapons']
        crew_list     = Data_CONST.get_text_list('SHIP_EXP_LEVEL')
        crew_exp_txt  = "%s (%d)" % (crew_list[ship.i_crew_quality], ship.i_crew_experience)
        shield_txt    = Data_CONST.get_text_list('SHIELDS')[design['shield']]

        xpos_1 = 15   # column 1
        xpos_2 = 170  # column 2
        ypos   = 285

        self.write_text(K_FONT5, K_PALETTE_SHIP_INFO, xpos_1, ypos +0,  design['name'])
        self.write_text(K_FONT4, K_PALETTE_SHIP_INFO, xpos_1, ypos +15, crew_exp_txt)
        self.write_text(K_FONT4, K_PALETTE_SHIP_INFO, xpos_1, ypos +30, shield_txt)
        self.write_text(K_FONT4, K_PALETTE_SHIP_INFO, xpos_1, ypos +50, "Beam OCV:")
        self.write_text(K_FONT4, K_PALETTE_SHIP_INFO, xpos_2, ypos +50, "Beam DCV:")
# ------------------------------------------------------------------------------
    def scroll_up(self, step=1):
        return
# ------------------------------------------------------------------------------
    def scroll_down(self, step=1):
        return
# ------------------------------------------------------------------------------
    def view_another_fleet(self, change):
        self.i_fleet_shown += change
        if self.i_fleet_shown >= self.i_num_fleets:
            self.i_fleet_shown = 0
        elif self.i_fleet_shown < 0:
            self.i_fleet_shown = self.i_num_fleets - 1
        self.reset_triggers_list()
        self.draw()
# ------------------------------------------------------------------------------
    def process_trigger(self, trigger):
        s_action = trigger['action']
        if s_action == "SCROLL_UP":
            self.scroll_up()
        elif s_action == "SCROLL_DOWN":
            self.scroll_down()
        elif s_action == "NEXT_FLEET":
            self.view_another_fleet(1)
        elif s_action == "PREVIOUS_FLEET":
            self.view_another_fleet(-1)
        elif s_action == "ship_info":
            self.display_ship_info(trigger['ship'])
# ------------------------------------------------------------------------------
Screen = Gui_FleetScreen()
