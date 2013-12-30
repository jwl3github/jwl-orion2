import pygame
import Gui_Screen

# ==============================================================================
class Gui_TextBox(Gui_Screen.Gui_Screen):
# ------------------------------------------------------------------------------
    def __init__(self):
        super(Gui_TextBox,self).__init__()
        self.i_x          = 139
        self.i_y          = 150
        self.s_title      = ''
        self.v_text_lines = []
# ------------------------------------------------------------------------------
    def reset_triggers_list(self):
        super(Gui_TextBox,self).reset_triggers_list()
        self.add_trigger({'action': "ESCAPE", 'rect': pygame.Rect((556, 459), ( 72, 20))})
# ------------------------------------------------------------------------------
    def draw(self):
        # draws a MOO2 textbox of varying size -- at position x,y -- big enough to output all strings in lines[]
        lines              = self.v_text_lines
        title              = self.s_title
        x                  = self.i_x
        y                  = self.i_y
        screen_width       = 640
        screen_height      = 480
        mid_part_width     = self.get_image('text_box', 'top').get_width()
        mid_part_height    = 10 + 15 * len(lines)
        off_y1             = self.get_image('text_box','top').get_height()
        off_y2             = mid_part_height + off_y1
        y3                 = self.get_image('text_box', 'bottom').get_height()

        # kludge? Correction for outsized boxes, where the bottom would have ended up outside of screen area
        bottom_box_boundary = y + mid_part_height + off_y1 +y3
        if bottom_box_boundary > screen_height:
            y = y - (bottom_box_boundary - screen_height)

        y1     = y + off_y1
        y2     = y + off_y2
        temp_r = pygame.Rect((1, 1),(1 + mid_part_width, 1 + mid_part_height))

        self.blit_image((x, y),   'text_box','top'),
        self.blit_image((x, y1),  'text_box','middle')  # JWL: what is temp_r ???
        self.blit_image((x, y2),  'text_box','bottom')

        self.write_text(K_FONT5, LIGHT_TEXT_PALETTE, x + 120, y + 20, title)

        lheight = 40
        for i in range(len(lines)):
        #   TODO: some intelligent way of justifying the lines, so the output resembles the original game
            self.write_text(K_FONT3, DARK_TEXT_PALETTE, x + 40, y + lheight, lines[i])
            lheight += 15

        self.reset_triggers_list()
        self.add_trigger({'action': "ESCAPE",  'rect': pygame.Rect((0, 0), ( 640, 480))})
# ------------------------------------------------------------------------------
Screen = Gui_TextBox()
