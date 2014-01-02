import pygame
import Gui_Screen
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
# ------------------------------------------------------------------------------
    def open_colony(self, i_colony_id):
        self.i_colony_id = i_colony_id
        self.o_colony    = self.get_colony(self.i_colony_id)
        self.i_planet_id = self.o_colony.i_planet_id
        self.o_planet    = self.get_planet(self.i_planet_id)
        self.i_star_id   = self.o_planet.i_star_id
        self.o_star      = self.get_star(self.i_star_id)
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

        self.blit(self.get_image('background', 'starfield'), (0, 0))
        self.blit(self.get_planet_background(planet.i_terrain, planet.i_picture), (0, 0))
        self.blit(self.get_image('colony_screen', 'panel'), (0, 0))

        self.reset_triggers_list()
        self.add_trigger({'action': "screen", 'screen': "colony_production", 'colony_id': colony_id, 'rect': pygame.Rect((519, 123), ( 61, 22))})

        ICON_AND_Y_OFFSET = { K_FARMER: (1,62), K_WORKER: (3,92), K_SCIENTIST: (5,122) }

        for i in range(K_MAX_STAR_OBJECTS):
            object_id = star.v_object_ids[i]
            if object_id != 0xFFFF:
                object = PLANETS[object_id]
                print "type: %i" % object.i_type

                if object.is_asteroid_belt():
                    x = 6
                    y = 22 + (24 * i)
                    self.blit(self.get_image('colony_screen', 'asteroids_scheme'), (x, y))
                    self.write_text(K_FONT2, K_PALETTE_SCHEMES_FONT, x + 29, y + 9, "Asteroids")

                if object.is_gas_giant():
                    x = 11
                    y = 27 + (24 * i)
                    self.blit(self.get_image('colony_screen', 'gasgiant_scheme'), (x, y))
                    write_text(K_FONT2, K_PALETTE_SCHEMES_FONT, x + 24, y + 4,  "Gas Giant -")
                    write_text(K_FONT2, K_PALETTE_SCHEMES_FONT, x + 24, y + 15, "uninhabitable")

                elif object.is_planet():
                    terrain = object.i_terrain
                    size = object.i_size
                    x = 10 + [6, 4, 3, 1, 0][size]
                    y = 26 + (24 * i) + [6, 4, 2, 1, 0][size]
                    self.blit(self.get_image('planet_scheme', terrain, size), (x, y))

            self.blit(self.get_image('colony_screen', 'scheme_arrow'), (6,  31 + (24 * i)))

        title_text    = "%s of %s" % (Data_CONST.get_text_list('COLONY_ASSIGNMENT')[colony.i_assignment], colony.s_name)
        title_surface = self.render(K_FONT5, K_PALETTE_TITLE, title_text, 2)
        (tw, th)      = title_surface.get_size()

        self.blit(title_surface, (320 - (tw / 2), 1))

        total_population = (1000 * colony.i_population) + sum(colony.v_pop_raised)
        print
        print "    Colony:        %s" % colony.s_name
        print "    Population:    %i (+%i)" % (total_population, sum(colony.v_pop_grow))
        print "    Food (result): %i (%i)" % (colony.i_food, colony.i_food - total_population)
        print "    Industry:      %i" % colony.i_industry
        print "    Research:      %i" % colony.i_research

        player_government_id = PLAYERS[colony.i_owner_id].get_racepick_item('goverment')

        self.blit(self.get_image('government', 'icon', player_government_id), (310, 32))

        # TODO: implement negative morale
        self.repeat_draw(340, 35, self.get_image('morale_icon', 'good'), colony.i_morale // 10, 30, 7, 155)

        x = 10 + self.repeat_draw(128, 64, self.get_image('production_10food'), colony.i_food // 10, 20, 6, 98)
        self.repeat_draw(x, 64, self.get_image('production_1food'), colony.i_food % 10, 20, 6, 98)

        # industry icons
        number = (colony.i_industry // 10) + (colony.i_industry % 10)
        xx = min(int(round(160 / max(1, number))), 20)
        x = self.repeat_draw(128, 94, self.get_image('production_10industry'), colony.i_industry // 10, xx, 99, 162)
        self.repeat_draw(x, 94, self.get_image('production_1industry'), colony.i_industry % 10, xx, 99, 162)

        # research icons
        number = (colony.i_research // 10) + (colony.i_research % 10)
        xx = min(int(round(160 / max(1, number))), 20)
        #print "### colony_screen::draw ... research icons ... number = %i, xx = %i" % (number, xx)
        x = self.repeat_draw(128, 124,self.get_image('production_10research'), colony.i_research // 10, xx, 99, 162)
        self.repeat_draw(x, 124, self.get_image('production_1research'), colony.i_research % 10, xx, 99, 162)

        for t in (K_FARMER, K_WORKER, K_SCIENTIST):
            c = len(colony.d_colonists[t])
            xx = 30 if c < 7 else 190/c
            icon, y = ICON_AND_Y_OFFSET[t]

            for i in range(c):
                colonist = colony.d_colonists[t][i]
                picture  = PLAYERS[colonist.race].i_picture
                x = 310 + xx * i
                self.blit(self.get_image('race_icon', picture, icon), (x, y))
                if i == (c - 1):
                    xx = 28 # enlarge the Rect of last icon (no other icon is drawn over it...)
                self.add_trigger({'action': "pick-colonist:%.2x:%i" % (t, (c - i)), 'rect': pygame.Rect((x, y), (xx, 28))})

        x = 0
        for i in range(colony.i_num_marines):
            self.blit_image((x, 450), 'race_icon', picture, 0x07)
            x += 30

        # TODO: count in all races not just owner!
        total_population   = (1000 * colony.total_population()) + sum(colony.v_pop_raised)
        pop_text           = "Pop %i,%.3i k (+%i)" % ((total_population // 1000), (total_population % 1000), sum(colony.v_pop_grow))
        population         = self.render(K_FONT3, K_PALETTE_POPULATION, pop_text, 2)
        (tw, th)           = population.get_size()

        self.blit(population, (529, 3))
# ------------------------------------------------------------------------------
    def process_trigger(self, o_trigger):

        i_colony_id = self.i_colony_id
        o_colony    = self.get_colony(i_colony_id)
        i_planet_id = colony.i_planet_id
        o_planet    = self.get_planet(i_planet_id)
        i_star_id   = planet.i_star_id
        o_star      = self.get_star(i_star_id)

        if o_trigger['action'] == "summary":
            s_summary = o_trigger['summary']

            if s_summary == "morale":
                text_box.Screen.set_title("Morale Summary")
                text_box.Screen.set_content(colony.print_morale_summary())

            elif s_summary == "bc":
                text_box.Screen.set_title("BC Summary")
                text_box.Screen.set_content(colony.print_bc_summary())

            elif s_summary == "food":
                text_box.Screen.set_title("Food Summary")
                text_box.Screen.set_content(colony.print_food_summary())

            elif s_summary == "industry":
                text_box.Screen.set_title("Industry Summary")
                text_box.Screen.set_content(colony.print_industry_summary())

            elif s_summary == "research":
                text_box.Screen.set_title("Research Summary")
                text_box.Screen.set_content(colony.print_research_summary())

            self.run_screen(text_box.Screen)
            self.redraw_flip()
# ------------------------------------------------------------------------------
Screen = Gui_ColonyScreen()
