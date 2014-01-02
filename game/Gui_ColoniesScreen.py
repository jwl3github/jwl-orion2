import pygame
import Gui_Screen
from Data_CONST import *


# ==============================================================================
class Gui_ColoniesScreen(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    __view_size  = 10
    __list_start = 0
    __list_size  = 0
# ------------------------------------------------------------------------------
    def __init__(self):
        super(Gui_ColoniesScreen,self).__init__()
# ------------------------------------------------------------------------------
    def reset_triggers_list(self):
        super(Gui_ColoniesScreen,self).reset_triggers_list()
        self.add_trigger({'action': "ESCAPE",       'rect': pygame.Rect((534, 448), (77, 19))})
        self.add_trigger({'action': "SCROLL_UP",    'rect': pygame.Rect((620, 16),  (8, 18))})
        self.add_trigger({'action': "SCROLL_DOWN",  'rect': pygame.Rect((620, 318), (8, 18))})
# ------------------------------------------------------------------------------
    def process_trigger(self, trigger):
        s_action = trigger['action']

        if s_action == "SCROLL_UP":
            self.scroll_up()

        elif s_action == "SCROLL_DOWN":
            self.scroll_down()
# ------------------------------------------------------------------------------
    def draw(self):
        PLAYERS  = self.list_players()
        COLONIES = self.list_colonies()
        RULES    = self.get_rules()

        self.draw_image_by_key((0, 0), 'colonies_screen.panel')

        print 'Check colonies for screen...'
        my_colonies = []
        for colony_id, colony in COLONIES.items():
            if (colony.i_owner_id == self.get_player_id()) and (not colony.is_outpost()):
                my_colonies.append("%s:%i" % (COLONIES[colony_id].s_name, colony_id))

        print my_colonies
        my_colonies.sort()
        for i in range(len(my_colonies)):
            colony_id = int(my_colonies[i].split(":")[1])
            my_colonies[i] = COLONIES[colony_id]

        self.__list_size = len(my_colonies)

        ICON_AND_XOFFSET = {K_FARMER: (1,101), K_WORKER: (3,236), K_SCIENTIST: (5, 378)}

        for i in range(self.__list_start, min(self.__list_size, self.__list_start + self.__view_size)):
            colony    = my_colonies[i]
            colony_id = colony.i_id
            planet_id = colony.i_planet_id

            if planet_id == 0xffff:
                print colony
                continue

            y = 38 + (31 * (i - self.__list_start))

            self.add_trigger({'action': "screen", 'screen': "colony", 'colony_id': colony_id, 'rect': pygame.Rect((12, y), (85, 24))})

            # production
            colony.debug_production(RULES)  # JWL - how to get turns to completion in colonies display??
            industry_progress  = colony.i_industry_progress
            industry           = colony.i_industry
            if industry == 0:
                industry == 0.001  # Prevent div-by-zero crash

            build_item = colony.get_build_item()
            if build_item:
                production_id   = build_item['production_id']
                production_name = RULES['buildings'][production_id]['name']
                production_cost = RULES['buildings'][production_id]['cost']
                turns           = (production_cost - industry_progress) / industry
                turns           = 1 if turns < 1 else int(turns + 0.99)
                turns           = 9999 if turns > 9999 else turns
                turns_txt       = "    %d turns" % turns
                self.write_text(K_FONT2, K_PALETTE_BUILD_ITEM, 512, y, production_name)
                self.write_text(K_FONT2, K_PALETTE_BUILD_ITEM, 512, y+10, turns_txt)
            else:
                self.write_text(K_FONT2, K_PALETTE_BUILD_ITEM, 512, y, '<none>')

            self.add_trigger({'action': "screen", 'screen': "colony_production", 'colony_id': colony_id, 'rect': pygame.Rect((513, y), (85, 24))})

            self.write_text(K_FONT3, K_PALETTE_BUILD_ITEM, 12, y + 5, colony.s_name, 2)

            for t in (K_FARMER, K_WORKER, K_SCIENTIST):
                c = len(colony.d_colonists[t])
                icon, x = ICON_AND_XOFFSET[t]
                xx = 28 if c < 5 else 114/c

                print 'Need to display colonists: %d' % c

                for ii in range(c):
                    colonist = colony.d_colonists[t][ii]
                    race     = colonist.race
                    picture  = PLAYERS[race].i_picture
                    self.draw_image_by_key((x + (xx * ii), y), 'race_icon', picture, icon)
# ------------------------------------------------------------------------------
    def scroll_up(self, step = 1):
        old_start = self.__list_start
        self.__list_start = max(0, self.__list_start - step)
        if old_start != self.__list_start:
            self.redraw_flip()
# ------------------------------------------------------------------------------
    def scroll_down(self, step = 1):
        old_start = self.__list_start
        self.__list_start = min(self.__list_start + step, self.__list_size - self.__view_size + 1)
        if old_start != self.__list_start:
            self.redraw_flip()
# ------------------------------------------------------------------------------
Screen = Gui_ColoniesScreen()
