import pygame
import Gui_Screen
from Data_CONST import *

# ==============================================================================
class Gui_ResearchScreen(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    def __init__(self):
        super(Gui_ResearchScreen,self).__init__()
# ------------------------------------------------------------------------------
    def draw(self):
        RULES             = self.get_rules()
        ME                = self.get_me()
        research_areas    = ME.v_research_areas
        hover             = self.get_hover()
        tech_color        = 0x047800
        tech_hover_color  = 0x28c800
        tech_active_color = 0x64d000

        self.reset_triggers_list()
        self.blit_image((80, 0), 'research_screen', 'panel')

        print 'draw -- '
        print ME
        print research_areas

        for research in research_areas:
            research_index = RULES['research'][research]['index']
            first_tech_id  = research_areas[research][0]
            first_tech     = RULES['tech_table'][first_tech_id]
            i_area_id      = first_tech['area']

            if ME.i_research_area == i_area_id:
                color = tech_active_color
            else:
                color = tech_color

            x = 95 + (227 * (research_index % 2))
            y = 51 + (105 * (research_index // 2))

            s_area_name = RULES['research_areas'][i_area_id]['name']
            self.write_text(K_FONT5, [0x0, 0x181818, color, color], x, y, s_area_name, 2)

            i = 0
            y += 19
            x += 10
            for tech_id in research_areas[research]:
                if (hover is not None) and (hover['action'] == "set_research") and (hover['tech_id'] == tech_id):
                    write_color = tech_hover_color
                else:
                    write_color = color

                s_tech_name = RULES['tech_table'][tech_id]['name']
                label = self.render(K_FONT4,  [0x0, 0x181818, write_color], s_tech_name, 2)

                yy = i * 15
                self.blit(label, (x, y + yy))
                self.add_trigger({'action': "set_research", 'tech_id': tech_id, 'rect': pygame.Rect((x, y + yy), label.get_size())})
                i += 1
# ------------------------------------------------------------------------------
    def process_trigger(self, trigger):
        if trigger['action'] == "set_research":
            tech_id = trigger['tech_id']
            self.set_research(tech_id)
            return self.get_escape_trigger()
# ------------------------------------------------------------------------------
Screen = Gui_ResearchScreen()
