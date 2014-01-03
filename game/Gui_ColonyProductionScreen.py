import copy
import pygame
import Data_BUILDINGS
import Gui_Screen
import Network_Client
from Data_CONST import *
# ==============================================================================
class Gui_ColonyProductionScreen(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    def __init__(self):
        Gui_Screen.Gui_Screen.__init__(self)
        self.i_colony_id = 0
        self.o_colony    = None
        self.i_planet_id = 0
        self.o_planet    = None
        self.i_star_id	 = 0
        self.o_star      = None
# ------------------------------------------------------------------------------
    def open_colony(self, colony_id):
        self.i_colony_id = colony_id
        self.o_colony    = self.get_colony(colony_id)
        print 'first'
        print colony_id
        print self.o_colony.serialize()
        self.i_planet_id = self.o_colony.i_planet_id
        self.o_planet    = self.get_planet(self.i_planet_id)
        self.i_star_id	 = self.o_planet.i_star_id
        self.o_star      = self.get_star(self.i_star_id)
# ------------------------------------------------------------------------------
    def reset_triggers_list(self):
        super(Gui_ColonyProductionScreen,self).reset_triggers_list()
        self.add_trigger({'action': "ESCAPE",  'hover_id': "ESCAPE",  'rect': pygame.Rect((494, 448), (58, 16))})
        self.add_trigger({'action': "CONFIRM", 'hover_id': "CONFIRM", 'rect': pygame.Rect((563, 448), (58, 16))})
# ------------------------------------------------------------------------------
    def hack_production_list(self, item_id, prod_list, pos, always_present):
        if item_id in prod_list:
            i = prod_list.index(item_id)
            prod_list.pop(i)
            if not always_present:
                prod_list.insert(pos, item_id)
        if always_present:
            prod_list.insert(pos, item_id)
# ------------------------------------------------------------------------------
    def draw(self):
        star                = self.o_star
        planet              = self.o_planet
        colony              = self.o_colony
        RULES               = self.get_rules()
        PROTOTYPES          = self.list_prototypes()
        ME                  = self.get_me()
        build_queue         = colony.v_build_queue

        self.reset_triggers_list()

        self.blit(self.get_image('background', 'starfield'), (0, 0))
        self.blit(self.get_planet_background(planet.i_terrain, planet.i_picture), (0, 0))

        shadow = pygame.Surface((640, 480))
    #   shadow.fill((0, 0, 0))
    #   shadow.fill((8, 8, 20))
        shadow.fill((28, 32, 44))
        shadow.set_alpha(128)
        self.blit(shadow, (0, 0))

    #    c1 = (0, 0, 0, 128)
    #    c1 = (8, 8, 20, 128)
        c1 = (28, 32, 44, 128)

        for y in range(0, 480, 2):
            self.draw_line(c1, (0, y), (639, y), 1)

    #    for x in range(0, 640, 2):
    #        self.draw_line(c1, (x, 0), (x, 479), 1)

        self.blit(self.get_image('colony_build_screen', 'panel'), (0, 0))

        #self.hack_production_list(254, available['building'], 0, True)   # Trade Goods first
        #self.hack_production_list(253, available['building'], 1, True)   # Housing second
        #self.hack_production_list(214, available['xship'],    0, False)  # Freighter Fleet
        #self.hack_production_list(246, available['special'], -1, False)  # Colony Base
        #self.hack_production_list(246, available['special'], -1, True)   # Spy

	# limit listing to 25 items here, overflow causes crash on Solaris, Python 2.6.5, Pygame 1.8.1
        print colony.serialize()
        v_left  = colony.d_available_production['trade'] + \
                  colony.d_available_production['housing'] + \
                  colony.d_available_production['building'][:25]
        v_right = colony.d_available_production['special'] + \
                  colony.d_available_production['xship']

        y = 20
        for i_id in v_left:
            s_name     = RULES['buildings'][i_id]['name']
            s_hover_id = "production:%i" % i_id
            if colony.in_build_queue(i_id):
                print 'Build-in-q: ' + s_name
                self.write_text(K_FONT3, K_PALETTE_LIGHT_TEXT, 13, y, s_name, 2)
                self.add_trigger({'action': "delete_production", 'production_id': i_id, 'hover_id': s_hover_id, 'rect': pygame.Rect((13, y), (170, 12))})
            else:
                print 'Build-not-in-q: ' + s_name
                self.write_text(K_FONT3, K_PALETTE_DARK_TEXT, 13, y, s_name, 2)
                self.add_trigger({'action': "production", 'production_id': i_id, 'hover_id': s_hover_id, 'rect': pygame.Rect((13, y), (170, 12))})
            y += 18

        y = 20
        for i_id in v_right:
            s_name     = RULES['buildings'][i_id]['name']
            s_hover_id = "production:%i" % i_id
            print 'Other: ' + s_name
            self.write_text(K_FONT5, K_PALETTE_LIGHT_TEXT, 485, y, s_name, 2)
            self.add_trigger({'action': "production", 'production_id': i_id, 'hover_id': s_hover_id, 'rect': pygame.Rect((485, y), (143, 15))})
            y += 19

        label = self.render(K_FONT4, K_PALETTE_LIGHT_TEXT, "Build List for %s" % colony.s_name, 2)
        self.blit(label, (240, 311))

        y = 334
        i = 0
        repeat = False
        for i_building_id in build_queue:
            if i_building_id < 0xFF:
                if i_building_id == Data_BUILDINGS.B_REPEAT:
                    repeat = True
                    continue

                production_name = RULES['buildings'][i_building_id]['name']
                label = self.render(K_FONT4, K_PALETTE_LIGHT_TEXT, production_name, 2)
                xx = (250 - label.get_width()) / 2
                self.blit(label, (208 + xx, y))
                hover_id = "queue:%i" % i
                if repeat:
                    self.add_trigger({'action': "delete_repeat_production", 'item': i, 'hover_id': hover_id, 'rect': pygame.Rect((208, y - 1), (250, 15))})
                    y += 20
                    label = self.render(K_FONT4, K_PALETTE_LIGHT_TEXT, "^ Repeat ^", 2)
                    xx = (250 - label.get_width()) / 2
                    self.blit(label, (208 + xx, y))
                    self.add_trigger({'action': "delete_repeat_production", 'item': i, 'hover_id': hover_id, 'rect': pygame.Rect((208, y - 1), (250, 15))})
                    repeat = False
                else:
                    self.add_trigger({'action': "delete_production", 'production_id': i_building_id, 'item': i, 'hover_id': hover_id, 'rect': pygame.Rect((208, y - 1), (250, 15))})
                y += 20
            i += 1

        return ######################## <<<<<<<<<<<<<<<<<<<<<<  TODO everything below

        yy = 0
        for i in range(5):
            prototype = PROTOTYPES[i]
            label_surface = FONTS['font_14_bold'].render(prototype['name'], 1, (0xE4, 0x88, 0x20))
            yy += 19
            self.blit(label_surface, (484, 110 + yy))

        build_queue = colony.v_build_queue
        yy = 0
        for queue_item in build_queue:
            build_id = queue_item['item']
            if build_id <  255:
                if build_id == 150:                  # ship design # x
                    label = PROTOTYPES[0]['name']
                elif build_id == 148:
                    label = PROTOTYPES[1]['name']
                elif build_id == 147:
                    label = PROTOTYPES[2]['name']
                elif build_id == 145:
                    label = PROTOTYPES[3]['name']
                elif build_id == 144:
                    label = PROTOTYPES[4]['name']
                else:
                    label = BUILDINGS[build_id]['name']

                label_surface = FONTS['font_12_bold'].render(label, 1, (0xE4, 0x88, 0x20))
                xx = label_surface.get_width() // 2
                self.blit(label_surface, (208 + 126 - xx, 332 + yy))
                yy += 20
# ------------------------------------------------------------------------------
    def process_trigger(self, trigger):
        """ Colony production screen implements following triggers:

            "production" = add production_id to the build queue
        """

        s_action = trigger['action']
        if s_action == "production":
            print("    action: %s" % s_action)
            print("        production: %i" % trigger['production_id'])
            self.o_colony.add_build_item(trigger['production_id'])
            self.redraw_flip()

        elif s_action == "delete_production":
            print("    action: %s" % s_action)
            print("        production: %i" % trigger['production_id'])
            self.o_colony.remove_build_item(trigger['production_id'])
            self.redraw_flip()
# ------------------------------------------------------------------------------
    def enter(self):
        self.__old_build_queue = copy.copy(self.o_colony.v_build_queue)
# ------------------------------------------------------------------------------
    def leave_confirm(self):
        Network_Client.Client.set_colony_build_queue(self.i_colony_id, self.o_colony.v_build_queue)
# ------------------------------------------------------------------------------
    def leave_cancel(self):
        self.o_colony.v_build_queue = self.__old_build_queue
# ------------------------------------------------------------------------------
Screen = Gui_ColonyProductionScreen()
