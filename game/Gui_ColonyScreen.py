import pygame
import Gui_Screen
import Gui_TextBox
import Network_Client
import Data_CONST
from Data_CONST import *

# ==============================================================================
class Gui_ColonyScreen(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    def __init__(self):
        Gui_Screen.Gui_Screen.__init__(self)
        self.i_colony_id = -1
        self.o_colony    = None
        self.i_planet_id = -1
        self.o_planet    = None
        self.i_star_id   = -1
        self.o_star      = None
        self.i_move_from_colonist_type  = 0
        self.i_move_from_colonist_index = 0
# ------------------------------------------------------------------------------
    def open_colony(self, i_colony_id):
        self.i_colony_id = i_colony_id
        self.o_colony    = self.get_colony(self.i_colony_id)
        self.i_planet_id = self.o_colony.i_planet_id
        self.o_planet    = self.get_planet(self.i_planet_id)
        self.i_star_id   = self.o_planet.i_star_id
        self.o_star      = self.get_star(self.i_star_id)
        self.i_move_from_colonist_type  = 0
        self.i_move_from_colonist_index = 0
# ------------------------------------------------------------------------------
    def reset_triggers_list(self):
        super(Gui_ColonyScreen,self).reset_triggers_list()
        self.add_trigger({'action': "ESCAPE",                         'rect': pygame.Rect((556, 459), ( 72, 20))})
        self.add_trigger({'action': "leaders",                        'rect': pygame.Rect((556, 427), ( 72, 20))})
        self.add_trigger({'action': "buy",                            'rect': pygame.Rect((590, 123), ( 37, 22))})
        self.add_trigger({'action': "summary", 'summary': "morale",   'rect': pygame.Rect((309,  31), (202, 25))})
        self.add_trigger({'action': "summary", 'summary': "bc",       'rect': pygame.Rect((127,  31), (177, 25))})
        self.add_trigger({'action': "summary", 'summary': "food",     'rect': pygame.Rect((127,  61), (177, 25))})
        self.add_trigger({'action': "summary", 'summary': "industry", 'rect': pygame.Rect((127,  91), (177, 25))})
        self.add_trigger({'action': "summary", 'summary': "research", 'rect': pygame.Rect((127, 121), (177, 25))})
# ------------------------------------------------------------------------------
    def draw(self):
        PLAYERS    = self.list_players()
        PLANETS    = self.list_planets()
        star       = self.o_star
        planet     = self.o_planet
        colony     = self.o_colony
        colony_id  = colony.i_id
        actual_pop = (1000 * colony.i_population) + sum(colony.v_pop_raised)

        print
        print "    Colony:        %s" % colony.s_name
        print "    Population:    %i (+%i)" % (actual_pop, sum(colony.v_pop_grow))
        print "    Food (result): %i (%i)" % (colony.i_food, colony.i_food - actual_pop)
        print "    Industry:      %i" % colony.i_industry
        print "    Research:      %i" % colony.i_research

        self.reset_triggers_list()
        self.add_trigger({'action': "screen", 'screen': "colony_production", 'colony_id': colony_id, 'rect': pygame.Rect((519, 123), ( 61, 22))})

        # Background and starfield
        self.blit(self.get_image('background', 'starfield'), (0, 0))
        self.blit(self.get_planet_background(planet.i_terrain, planet.i_picture), (0, 0))
        self.blit(self.get_image('colony_screen', 'panel'), (0, 0))

        # Solar system objects list
        for i in range(K_MAX_STAR_OBJECTS):
            self.blit(self.get_image('colony_screen', 'scheme_arrow'), (6,  31 + (24 * i)))
            object_id = star.v_object_ids[i]
            if object_id != 0xFFFF:
                o_object = PLANETS[object_id]

                if o_object.is_asteroid_belt():
                    x = 6
                    y = 22 + (24 * i)
                    self.blit(self.get_image('colony_screen', 'asteroids_scheme'), (x, y))
                    self.write_text(K_FONT2, K_PALETTE_SCHEMES_FONT, 40, y + 5, "Asteroids")

                if o_object.is_gas_giant():
                    x = 11
                    y = 27 + (24 * i)
                    self.blit(self.get_image('colony_screen', 'gasgiant_scheme'), (x, y))
                    self.write_text(K_FONT2, K_PALETTE_SCHEMES_FONT, 40, y + 5,  "Gas Giant")

                elif o_object.is_planet():
                    x = 10 + [6, 4, 3, 1, 0][o_object.i_size]
                    y = 26 + (24 * i) + [6, 4, 2, 1, 0][o_object.i_size]
                    self.blit(self.get_image('planet_scheme', o_object.i_terrain, o_object.i_size), (x, y))
                    self.write_text(K_FONT2, K_PALETTE_SCHEMES_FONT, 40, y + 5,  o_object.s_name)
                    ##JWL: TODO Also need triggers to switch view to this planet if it has a colony

        # Screen title / Population summary
        title_text    = "%s of %s" % (Data_CONST.get_text_list('COLONY_ASSIGNMENT')[colony.i_assignment], colony.s_name)
        title_surface = self.render(K_FONT5, K_PALETTE_TITLE, title_text, 2)
        (tw, th)      = title_surface.get_size()
        self.blit(title_surface, (320 - (tw / 2), 1))

        pop_text           = "Pop %i,%.3i k (%+i k)" % ((actual_pop // 1000), (actual_pop % 1000), sum(colony.v_pop_grow))
        population         = self.render(K_FONT3, K_PALETTE_POPULATION, pop_text, 2)
        (tw, th)           = population.get_size()
        self.blit(population, (520, 3))

        # government/morale icons
        player_government_id = PLAYERS[colony.i_owner_id].get_racepick_item('goverment')
        self.blit(self.get_image('government', 'icon', player_government_id), (310, 32))

        s_morale_type = 'good' if colony.i_morale > 100.0 else 'bad'
        i_morale_num = abs(colony.i_morale - 100.0) // 10
        self.repeat_draw(340, 35, self.get_image('morale_icon', s_morale_type), i_morale_num, 30, 7, 155)

        # Food icons
        #xx = 10
        number = (colony.i_food // 10) + (colony.i_food % 10)
        xx = min(int(round(160 / max(1, number))), 20)
        x  = self.repeat_draw(128, 64, self.get_image('production_10food'), colony.i_food // 10, xx, 99, 162) #6, 98)
        x  = self.repeat_draw(x,   64, self.get_image('production_1food'),  colony.i_food %  10, xx, 99, 162) #6, 98)
        # TODO missing (red outline) food

        # Industry icons
        number = (colony.i_industry // 10) + (colony.i_industry % 10)
        xx = min(int(round(160 / max(1, number))), 20)
        x  = self.repeat_draw(128, 94, self.get_image('production_10industry'), colony.i_industry // 10, xx, 99, 162)
        x  = self.repeat_draw(x,   94, self.get_image('production_1industry'),  colony.i_industry %  10, xx, 99, 162)

        # Research icons
        number = (colony.i_research // 10) + (colony.i_research % 10)
        xx = min(int(round(160 / max(1, number))), 20)
        x  = self.repeat_draw(128, 124, self.get_image('production_10research'), colony.i_research // 10, xx, 99, 162)
        x  = self.repeat_draw(x,   124, self.get_image('production_1research'),  colony.i_research %  10, xx, 99, 162)

        # Colonist icons
        ICON_AND_Y_OFFSET = { K_FARMER: (1,62), K_WORKER: (3,92), K_SCIENTIST: (5,122) }
        for t in (K_FARMER, K_WORKER, K_SCIENTIST):
            c = len(colony.d_colonists[t])
            xx = 30 if c < 7 else 190/c   # Adjust for normal versus overlapped colonist icons
            icon, y = ICON_AND_Y_OFFSET[t]

            for i in range(c):
                colonist = colony.d_colonists[t][i]
                picture  = PLAYERS[colonist.race].i_picture
                x = 310 + xx * i
                self.blit(self.get_image('race_icon', picture, icon), (x, y))
                if i == (c - 1):
                    xx = 28 # enlarge the Rect of last icon (no other icon is drawn over it...)
                self.add_trigger({'action': "pick-colonist:0x%.2x:%i" % (t, i), 'rect': pygame.Rect((x, y), (xx, 28))})

        # Marines / Armors / Mechs
        x = 0
        for i in range(colony.i_num_marines):
            self.blit_image((x, 450), 'race_icon', picture, 0x07)
            x += 30
        # TODO Armors/mechs

# ------------------------------------------------------------------------------
    def process_trigger(self, o_trigger):

        s_action = o_trigger['action']
        print 'Gui_ColonyScreen.process_trigger() - action = ' + s_action

        if s_action == "summary":

            Network_Client.Client.fetch_colony_prod_summary(self.o_colony.i_colony_id)
            s_summary = o_trigger['summary']

            if s_summary == "morale":
                Gui_TextBox.Screen.s_title = 'Morale Summary'
                Gui_TextBox.Screen.v_text_lines = self.o_colony.print_morale_summary()

            elif s_summary == "bc":
                Gui_TextBox.Screen.s_title = 'BC Summary'
                Gui_TextBox.Screen.v_text_lines = self.o_colony.print_bc_summary()

            elif s_summary == "food":
                Gui_TextBox.Screen.s_title = 'Food Summary'
                Gui_TextBox.Screen.v_text_lines = self.o_colony.print_food_summary()

            elif s_summary == "industry":
                Gui_TextBox.Screen.s_title = 'Industry Summary'
                Gui_TextBox.Screen.v_text_lines = self.o_colony.print_industry_summary()

            elif s_summary == "research":
                Gui_TextBox.Screen.s_title = 'Research Summary'
                Gui_TextBox.Screen.v_text_lines = self.o_colony.print_research_summary()
            else:
                return

            self.run_screen(Gui_TextBox.Screen)
            self.redraw_flip()
        elif s_action == 'leaders':
            print 'Gui_ColonyScreen: "leaders" action handling TBD'
        elif s_action == 'buy':
            print 'Gui_ColonyScreen: "buy" action handling TBD'
        elif s_action.startswith('pick-colonist'):
            c_tag, c_type, c_index = s_action.split(':')
            self.i_move_from_colonist_type  = int(c_type, 16)
            self.i_move_from_colonist_index = int(c_index)
            self.add_trigger({'action': "drop-colonist-food",     'rect': pygame.Rect((127,  61), (700, 25))}, True)
            self.add_trigger({'action': "drop-colonist-industry", 'rect': pygame.Rect((127,  91), (700, 25))}, True)
            self.add_trigger({'action': "drop-colonist-research", 'rect': pygame.Rect((127, 121), (700, 25))}, True)
            ##JWL: TODO Also need trigger to drop onto another planet.
            ##JWL: TODO maybe implement as a change-to-action-value for the existing 'view-planet' trigger
        elif s_action == 'drop-colonist-food':
            self.move_colonists_to(K_FARMER)
        elif s_action == 'drop-colonist-industry':
            self.move_colonists_to(K_WORKER)
        elif s_action == 'drop-colonist-research':
            self.move_colonists_to(K_SCIENTIST)
        else:
            print 'Gui_ColonyScreen: Do not know how to handle trigger action = ' + o_trigger['action']
# ------------------------------------------------------------------------------
    def move_colonists_to(self, new_job_type):
        t = self.i_move_from_colonist_type
        i = self.i_move_from_colonist_index
        print 'move_colonists_to -> t [%d] i [%d]  new_t [%d]' % (t, i, new_job_type)
        if t == 0:
            pass  # Invalid type.
        elif t == new_job_type:
            print 'Colonists moved back to same job.'
        elif (new_job_type == K_FARMER) and not self.o_colony.allows_farming():
            print 'Cannot have farmers on this planet. Job change ignored.'
        else:
            super(Gui_ColonyScreen,self).change_colonist_job(self.o_colony.i_colony_id,
                                                             self.i_move_from_colonist_type,
                                                             self.i_move_from_colonist_index,
                                                             new_job_type)
        self.i_move_from_colonist_type  = 0
        self.i_move_from_colonist_index = 0
        self.draw()
# ------------------------------------------------------------------------------
Screen = Gui_ColonyScreen()
