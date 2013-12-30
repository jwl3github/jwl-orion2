import pygame
import Gui_Screen
from Data_CONST import *

# ==============================================================================
class Gui_InfoScreen(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    def __init__(self):
        super(Gui_InfoScreen,self).__init__()
        self.__tech_review = "achievements"
# ------------------------------------------------------------------------------
    def reset_triggers_list(self):
        super(Gui_InfoScreen,self).reset_triggers_list()
        self.add_trigger({'action': "ESCAPE",  'rect': pygame.Rect((547, 441), ( 64, 17))})
# ------------------------------------------------------------------------------
    def draw(self):
        self.fill((0, 0, 0))
        self.blit_image((0, 0),   'info_screen', 'panel'),
        self.blit_image((21, 50), 'info_screen', 'button', 'history_graph',   'off'),
        self.blit_image((21, 77), 'info_screen', 'button', 'tech_review',     'off'),
        self.blit_image((21, 102),'info_screen', 'button', 'race_statistics', 'off'),
        self.blit_image((21, 128),'info_screen', 'button', 'turn_summary',    'off'),
        self.blit_image((21, 154),'info_screen', 'button', 'reference',       'off'),

        # grid behind
        self.blit_image((433, 115), 'app_pic', 0)

        # app image
        self.blit_image((433, 115), 'app_pic', 155)

        tech_carets = []

        if self.__tech_review == "achievements":

            v_known_techs = self.get_me().v_known_techs

            # New Construction Types
            items = []
            for tech_id in [K_TECH_PLANET_CONSTRUCTION, K_TECH_TITAN_CONTRUCTION, K_TECH_TRANSPORT, K_TECH_OUTPOST_SHIP, K_TECH_FREIGHTERS, K_TECH_COLONY_SHIP, K_TECH_COLONY_BASE]:
                if tech_id in v_known_techs:
                    items.append(tech_id)
            if len(items):
                tech_carets.append({'title': "New Construction Types", 'items': items})

            # Spies
            items = []
            for tech_id in [K_TECH_TELEPATHIC_TRAINING, K_TECH_NEURAL_SCANNER, K_TECH_SPY_NETWORK]:
                if tech_id in v_known_techs:
                    items.append(tech_id)
            if len(items):
                tech_carets.append({'title': "Spies", 'items': items})

        y = 64
        for caret in tech_carets:
            if len(caret['items']):
                self.write_text(K_FONT4, K_PALETTE_TECH, 223, y, caret['title'], 2)
                y += 16
                for item in caret['items']:
                    text = Data_CONST.get_text_list('TECH_LIST')[item]['name']
                    self.write_text(K_FONT3, K_PALETTE_TECH, 233, y, text, 2)
                    y += 13
                y += 6
# ------------------------------------------------------------------------------
Screen = Gui_InfoScreen()
