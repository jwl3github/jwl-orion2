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
            s_area_name    = RULES['research_areas'][i_area_id]['name']

            # Research area (category) title
            x = 95 + (227 * (research_index % 2))
            y = 51 + (105 * (research_index // 2))

            if ME.i_research_area == i_area_id:
                self.write_text(K_FONT5, K_PALETTE_TECH_ACTIVE, x, y, s_area_name, 2)
            else:
                self.write_text(K_FONT5, K_PALETTE_TECH_NORMAL, x, y, s_area_name, 2)

            i = 0
            y += 19
            x += 10
            for tech_id in research_areas[research]:
                if (hover is not None) and (hover['action'] == "set_research") and (hover['tech_id'] == tech_id):
                    write_palette = K_PALETTE_TECH_HOVER
                elif tech_id == ME.i_research_tech_id:
                    write_palette = K_PALETTE_TECH_ACTIVE
                else:
                    write_palette = K_PALETTE_TECH_NORMAL

                s_tech_name = RULES['tech_table'][tech_id]['name']
                label = self.render(K_FONT4,  write_palette, s_tech_name, 2)
                size  = label.get_size()
                self.blit(label, (x, y))
                self.add_trigger({'action': "set_research", 'tech_id': tech_id, 'rect': pygame.Rect((x, y), label.get_size())})
                i += 1
                y += label.get_height()
# ------------------------------------------------------------------------------
    def process_trigger(self, trigger):
        if trigger['action'] == "set_research":
            tech_id = trigger['tech_id']
            self.set_research(tech_id)
            return self.get_escape_trigger()
# ------------------------------------------------------------------------------
Screen = Gui_ResearchScreen()
