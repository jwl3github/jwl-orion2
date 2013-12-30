import pygame
import Gui_Screen
from Data_CONST import *


# ==============================================================================
class Gui_PlanetsScreen(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    def __init__(self):
        super(Gui_PlanetsScreen,self).__init__()
        self.__viewport_size    = 8
        self.__planet_list_pos  = 0
        self.planets_to_display = 0
# ------------------------------------------------------------------------------
    def reset_triggers_list(self):
        super(Gui_PlanetsScreen,self).reset_triggers_list()
        self.add_trigger({'action': "sort",   'sort': "climate",                   'rect': pygame.Rect((442, 200), (58, 25))})
        self.add_trigger({'action': "sort",   'sort': "minerals",                  'rect': pygame.Rect((502, 200), (64, 25))})
        self.add_trigger({'action': "sort",   'sort': "size",                      'rect': pygame.Rect((568, 200), (56, 25))})
        self.add_trigger({'action': "filter", 'filter': "no_enemy_presence",       'rect': pygame.Rect((444, 268), (177, 18))})
        self.add_trigger({'action': "filter", 'filter': "normal_gravity",          'rect': pygame.Rect((444, 291), (177, 18))})
        self.add_trigger({'action': "filter", 'filter': "non_hostile_environment", 'rect': pygame.Rect((444, 314), (177, 18))})
        self.add_trigger({'action': "filter", 'filter': "mineral_abundance",       'rect': pygame.Rect((444, 337), (177, 18))})
        self.add_trigger({'action': "filter", 'filter': "planets_in_range",        'rect': pygame.Rect((444, 360), (177, 18))})
        self.add_trigger({'action': "send_colony_ship",                            'rect': pygame.Rect((457, 390), (150, 18))})
        self.add_trigger({'action': "send_outpost_ship",                           'rect': pygame.Rect((457, 416), (150, 18))})
        self.add_trigger({'action': "ESCAPE",                                      'rect': pygame.Rect((457, 444), (150, 18))})
        self.add_trigger({'action': "SCROLL_UP",                                   'rect': pygame.Rect((422, 15),  (10, 20))})
        self.add_trigger({'action': "SCROLL_DOWN",                                 'rect': pygame.Rect((422, 447), (10, 20))})
        self.add_trigger({'action': "SCROLL_UP",                                   'rect': pygame.Rect((422, 35),  (12, 205))})
        self.add_trigger({'action': "SCROLL_DOWN",                                 'rect': pygame.Rect((422, 240), (12, 205))})
# ------------------------------------------------------------------------------
    def process_trigger(self, trigger):
        s_action = trigger['action']

        if s_action == "SCROLL_UP":
            if self.scroll_up():
                self.redraw_flip()

        elif s_action == "SCROLL_DOWN":
            if self.scroll_down():
                self.redraw_flip()
# ------------------------------------------------------------------------------
    def list_planets_to_display(self, player_id):
        planets = []
        for star_id, star in self.list_stars().items():
            if star.visited_by_player(player_id):
                for object_id in star.v_object_ids:
                    if object_id != 0xffff:
                        planet = self.get_planet(object_id)
                        if planet.is_planet():
                            planets.append(planet)
        return planets
# ------------------------------------------------------------------------------
    def scroll_up(self, step = 1):
        old_start = self.__planet_list_pos
        self.__planet_list_pos = max(0, self.__planet_list_pos - step)
        return old_start != self.__planet_list_pos
# ------------------------------------------------------------------------------
    def scroll_down(self, step = 1):
        old_start = self.__planet_list_pos
        self.__planet_list_pos = min(self.__planet_list_pos + step, len(self.__planets_list) - self.__viewport_size)
        return old_start != self.__planet_list_pos
# ------------------------------------------------------------------------------
    def draw(self):
        self.draw_image_by_key((0, 0), 'planets_screen.panel')

        self.__planets_list = self.list_planets_to_display(self.get_player_id())
        #TODO: sorting planets

        y = 37
        for planet in self.__planets_list[self.__planet_list_pos:self.__planet_list_pos + self.__viewport_size]:
            star_id        = planet.i_star_id
            name_t         = self.get_star(star_id).s_name
            terrain_t      = planet.get_terrain_text()
            minerals_t     = planet.get_minerals_text()
            size_t         = planet.get_size_text()
            gravity_t      = planet.get_gravity_text()
            name_label     = self.render(K_FONT3, K_PALETTE_VIEWPORT_FONT, name_t,     2)
            terrain_label  = self.render(K_FONT3, K_PALETTE_VIEWPORT_FONT, terrain_t,  2)
            gravity_label  = self.render(K_FONT3, K_PALETTE_VIEWPORT_FONT, gravity_t,  2)
            minerals_label = self.render(K_FONT3, K_PALETTE_VIEWPORT_FONT, minerals_t, 2)
            size_label     = self.render(K_FONT3, K_PALETTE_VIEWPORT_FONT, size_t,     2)
            planet_image   = self.get_image('starsystem_map', 'planet', planet.i_terrain, planet.i_size)
            ph             = (planet_image.get_height() // 2)

            self.draw_image((60  - (planet_image.get_width()   // 2), y + 28 - ph), planet_image)
            self.draw_image((60  - (name_label.get_width()     // 2), y + 28),      name_label)
            self.draw_image((140 - (terrain_label.get_width()  // 2), y + 11),      terrain_label)
            self.draw_image((217 - (gravity_label.get_width()  // 2), y + 11),      gravity_label)
            self.draw_image((311 - (minerals_label.get_width() // 2), y + 11),      minerals_label)
            self.draw_image((386 - (size_label.get_width()     // 2), y + 11),      size_label)

            #TODO: display industry, population sizes, food prod data, enemy presence...
            y += 55
# ------------------------------------------------------------------------------
Screen = Gui_PlanetsScreen()
