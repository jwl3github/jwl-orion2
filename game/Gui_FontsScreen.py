import Gui_Screen

class Gui_FontsScreen(Gui_Screen.Gui_Screen):

    def __init__(self):
        super(Gui_FontsScreen,self).__init__()
        self.reset_triggers_list()

    def draw(self):
        DISPLAY   = Gui_Screen.DISPLAY
        PALETTE1  = [0x0, 0x999999, 0xffffff, 0x333333, 0x00ff00, 0x0000ff, 0x00ffff, 0xff00ff, 0xffff00]
        all_fonts = self.get_all_fonts()
        font3     = all_fonts['font3']

        self.blit(self.get_image('main_screen', 'panel'), (0, 0))

        y = 30
        yy = 10
        for font_id, font in all_fonts.items():
            font.write_text(DISPLAY, 30, y, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", palette1)
            font.write_text(DISPLAY, 30, y + yy, "abcdefghijklmnopqrstuvwxyz", palette1)
            font.write_text(DISPLAY, 30, y + yy + yy, "0123456789 () [] {} +-/* ;'\",. <>? !@#$%^&*=~", palette1)
            yy += 2
            y += yy + yy + yy + 10

        stardate_palette = [0x0, 0x7c7c84, 0xbcbcc4]

        font3.write_text(self.get_display(), 561, 29, "3529.2", stardate_palette, 2)

        title = font3.render("Master of Orion II", palette1, 2)

        self.blit(title, (500, 40))

