import pygame
import Gui_Screen
from Data_CONST import *

# ==============================================================================
class Gui_LeadersScreen(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    def __init__(self):
        super(Gui_LeadersScreen,self).__init__()
        self.__type = 1
# ------------------------------------------------------------------------------
    def reset_triggers_list(self):
        super(Gui_LeadersScreen,self).reset_triggers_list()
        self.add_trigger({'action': "ESCAPE",        	 'rect': pygame.Rect((544, 445), (70, 18))})
        self.add_trigger({'action': "hire",         	 'rect': pygame.Rect((319, 445), (60, 18))})
        self.add_trigger({'action': "showColonyLeaders", 'rect': pygame.Rect((15, 14),   (135, 15))})
        self.add_trigger({'action': "showShipOfficers",	 'rect': pygame.Rect((160, 14),  (135, 15))})
# ------------------------------------------------------------------------------
    def process_trigger(self, trigger):
        s_action = trigger['action']

        if s_action == "showColonyLeaders" and self.__type == K_HERO_OFFICER:
            self.__type = K_HERO_GOVERNOR
            self.redraw_flip()

        elif s_action == "showShipOfficers" and self.__type == K_HERO_GOVERNOR:
            self.__type = K_HERO_OFFICER
            self.redraw_flip()
# ------------------------------------------------------------------------------
    def draw(self):
        STARS = self.list_stars()

        if self.__type == K_HERO_GOVERNOR:
            HEROES = self.list_governors()
            button = 'colony_leaders_button'
        else:
            HEROES = self.list_officers()
            button = 'ship_officers_button'

        self.reset_triggers_list()

        self.blit_image((0, 0), 'leaders_screen', 'panel')
        self.blit_image((7, 10), 'leaders_screen', button)

        i = -1
        for hero_id, hero in HEROES.items():
            i += 1

            if hero['location'] == 0xffff:
                location_text = "Officer Pool"
            elif self.__type == K_HERO_GOVERNOR:
                location_text = STARS[hero['location']].s_name
            else:
                location_text = "ship..."

            self.blit_image((13, 38 + (109 * i)), 'leader', 'face', hero['picture'])
            self.write_text(K_FONT4, K_PALETTE_COMMON, 125, 38 + (109 * i), hero['name'])

            location_surface = self.render(K_FONT3, K_PALETTE_COMMON, location_text, 2)
            text_width, text_height = location_surface.get_size()
            self.blit(location_surface, (49 - (text_width / 2), 131 + (109 * i)))

            skills = self.setup_skills(hero)
            skill_row = 0
            for skill in skills:
                y = 50 + (109 * i) + (17 * skill_row)
                self.blit_image((94, y), 'leader', 'skill_icon', skill[0])
                self.write_text(K_FONT4, K_PALETTE_COMMON, 116, y + 4, skill[1])
                skill_row += 1

# ------------------------------------------------------------------------------
    def setup_skills(hero):
        skills = []
        if hero['type'] == 0:		# ship leader skills
            if hero['special_skills'] & 4:
                skills.append(['fighter_pilot', "Fighter Pilot"])
            if hero['special_skills'] & 8:
                skills.append(['fighter_pilot', "Fighter Pilot*"])
            if hero['special_skills'] & 16:
                skills.append(['galactic_role', "Galactic Role"])
            if hero['special_skills'] & 32:
                skills.append(['galactic_role', "Galactic Role*"])
            if hero['special_skills'] & 64:
                skills.append(['helmsman', "Helmsman"])
            if hero['special_skills'] & 128:
                skills.append(['helmsman', "Helmsman*"])
            if hero['special_skills'] & 256:
                skills.append(['navigator', "Navigator"])
            if hero['special_skills'] & 512:
                skills.append(['navigator', "Navigator*"])
            if hero['special_skills'] & 1024:
                skills.append(['ordnance', "Ordnance"])
            if hero['special_skills'] & 2048:
                skills.append(['ordnance', "Ordnance*"])
            if hero['special_skills'] & 16384:
                skills.append(['weaponry', "Weaponry"])
            if hero['special_skills'] & 32768:
                skills.append(['weaponry', "Weaponry*"])

        elif hero['type'] == 1:		# colony leader skills
            if hero['special_skills'] & 16:
                skills.append(['financial_leader', "Financial Leader"])
            if hero['special_skills'] & 32:
                skills.append(['financial_leader', "Financial Leader*"])
            if hero['special_skills'] & 64:
                skills.append(['instructor', "Instructor"])
            if hero['special_skills'] & 128:
                skills.append(['instructor', "Instructor*"])
            if hero['special_skills'] & 256:
                skills.append(['labor_leader', "Labor Leader"])
            if hero['special_skills'] & 512:
                skills.append(['labor_leader', "Labor Leader*"])
            if hero['special_skills'] & 1024:
                skills.append(['medicine', "Medicine"])
            if hero['special_skills'] & 2048:
                skills.append(['medicine', "Medicine*"])
            if hero['special_skills'] & 4096:
                skills.append(['science_leader', "Science Leader"])
            if hero['special_skills'] & 8196:
                skills.append(['science_leader', "Science Leader*"])
            if hero['special_skills'] & 16384:
                skills.append(['spiritual_leader', "Spiritual Leader"])
            if hero['special_skills'] & 32768:
                skills.append(['spiritual_leader', "Spiritual Leader*"])
            if hero['special_skills'] & 65536:
                skills.append(['tactics', "Tactics"])
            if hero['special_skills'] & 131072:
                skills.append(['tactics', "Tactics*"])

        if hero['common_skills'] & 1:	# commond skills
            skills.append(['assassin', "Assassin"])
        if hero['common_skills'] & 2:
            skills.append(['assassin', "Assassin*"])
        if hero['common_skills'] & 4:
            skills.append(['commando', "Commando"])
        if hero['common_skills'] & 8:
            skills.append(['commando', "Commando*"])
        if hero['common_skills'] & 16:
            skills.append(['diplomat', "Diplomat"])
        if hero['common_skills'] & 32:
            skills.append(['diplomat', "Diplomat*"])
        if hero['common_skills'] & 64:
            skills.append(['famous', "Famous"])
        if hero['common_skills'] & 128:
            skills.append(['famous', "Famous*"])
        if hero['common_skills'] & 256:
            skills.append(['megawealth', "Megawealth"])
        if hero['common_skills'] & 512:
            skills.append(['megawealth', "Megawealth*"])
        if hero['common_skills'] & 1024:
            skills.append(['operations', "Operations"])
        if hero['common_skills'] & 2048:
            skills.append(['operations', "Operations*"])
        if hero['common_skills'] & 4096:
            skills.append(['researcher', "Researcher"])
        if hero['common_skills'] & 8192:
            skills.append(['researcher', "Researcher*"])
        if hero['common_skills'] & 16384:
            skills.append(['spy_master', "Spy Master"])
        if hero['common_skills'] & 32768:
            skills.append(['spy_master', "Spy Master*"])
        if hero['common_skills'] & 65536:
            skills.append(['telepath', "Telepath"])
        if hero['common_skills'] & 131072:
            skills.append(['telepath', "Telepath*"])
        if hero['common_skills'] & 262144:
            skills.append(['trader', "Trader"])
        if hero['common_skills'] & 524288:
            skills.append(['trader', "Trader*"])

# ------------------------------------------------------------------------------
Screen = Gui_LeadersScreen()
