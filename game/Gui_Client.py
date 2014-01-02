import pygame
from pygame.locals import *

import copy
import Moo2_LBX
import Gui_Screen
import Gui_SplashScreen
import Gui_MainScreen
import Gui_ColoniesScreen
import Gui_ColonyScreen
import Gui_ColonyProductionScreen
import Gui_PlanetsScreen
import Gui_LeadersScreen
import Gui_InfoScreen
import Gui_ResearchScreen
import Gui_StarsystemScreen
import Gui_FleetScreen
import Network_Client
import Data_CONST
from Data_CONST import *

LBX_MD5_FILEPATH     = 'C:\\Work\\jwl-orion2\\game\\lbx.md5'
GRAPHIC_INI_FILEPATH = 'C:\\Work\\jwl-orion2\\game\\graphic.ini'
REDRAW_MOUSE_EVENT   = pygame.USEREVENT + 1
ANIMATE_SCREEN_EVENT = pygame.USEREVENT + 2
MOUSE_EVENT_TIMER    = 40
ANIMATE_SCREEN_TIMER = 40

# ==============================================================================
class Gui_Client(object):

    __highlight_triggers = False
    __image_pool         = {}
    __mouse_cursor       = None
    __mouse_pos          = (0, 0)

# ------------------------------------------------------------------------------
    def __init__(self):
        self.graphic_ini = self.__read_text_file(GRAPHIC_INI_FILEPATH)
        self.highlight_triggers_on()
# ------------------------------------------------------------------------------
    def init(self, moo2_dir):
        self.moo2_dir = moo2_dir
        self.__load_lbx_archives()
        self.__load_fonts()
        self.__load_palettes()
        self.__load_graphic(self.graphic_ini[:1])
        self.__load_ships_lbx()
        pygame.init()
        pygame.display.set_mode((640, 480), 0, 24)
        self.DISPLAY = pygame.display.get_surface()
        screen = Gui_Screen.Gui_Screen()
        screen.init(self)
# ------------------------------------------------------------------------------
    def get_display(self):
        """Returns Pygame Display Surface object

        Will be removed in the near future

        """
        return pygame.display.get_surface()
# ------------------------------------------------------------------------------
    def highlight_triggers_on(self):
        """Enables the triggers highlightling"""
        self.b_highlight_triggers = True
# ------------------------------------------------------------------------------
    def highlight_triggers_off(self):
        """Disables the triggers highlightling"""
        self.b_highlight_triggers = False
# ------------------------------------------------------------------------------
    def flip(self, src = None):
        """Flips the display buffer content and redraws the mouse cursor"""
        if self.mouse_cursor:
            bg_area = pygame.Rect(self.mouse_pos, self.mouse_cursor_size)
            cursor_bg = pygame.Surface(self.mouse_cursor_size)
            cursor_bg.blit(self.DISPLAY, (0, 0), bg_area)
            self.DISPLAY.blit(self.mouse_cursor, self.mouse_pos)
            pygame.display.flip()
            self.DISPLAY.blit(cursor_bg, self.mouse_pos)
        else:
            pygame.display.flip()
# ------------------------------------------------------------------------------
    def update(self, rects = None):
        """Pushes given portions of graphic buffer to display"""
        pygame.display.update(rects)
# ------------------------------------------------------------------------------
    def __read_text_file(self, filename):
        """Returns the content of the given text file as a list of strings"""
        fh = open(filename, 'rt')
        content = fh.read().strip().split("\n")
        fh.close()
        return content
# ------------------------------------------------------------------------------
    def __load_lbx_archives(self):
        """Loads LBX archives listed in lbx.md5 file.

        The files are checked for a given MD5 sum.
        returns True if all loaded files match their expected checksum, otherwise returns False

        """
        print("Loading LBX archive index")
        self.lbx = {}
        lbx_md5 = self.__read_text_file(LBX_MD5_FILEPATH)
        check = True
        for line in lbx_md5:
            md5, filename = line.strip().split("  ")
            self.lbx[filename] = Moo2_LBX.Archive("%s/%s" % (self.moo2_dir, filename), md5)
            if self.lbx[filename].check_md5():
                print("    %s  %s ... OK" % (md5, filename))
            else:
                print("    %s  %s ... error" % (md5, filename))
                print("        MD5 sum does not match, actual MD5 sum is %s" % self.lbx[filename].md5_hexdigest())
                check = False
        print("")
        if check:
            print("    Done")
        else:
            print("    Done with LBX loading errors: (MD5 checksum mismatch)")
            #print("    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            #print("    Warning!")
            #print("")
            #print("    Some LBX files don't match the expected MD5 checksum")
            #print("    The OpenMOO2 supports only original LBX files from MOO2 version 1.31")
            #print("")
            #print("    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        return check
# ------------------------------------------------------------------------------
    def __load_fonts(self):
        """Loads up the game fonts"""
        self.fonts = {
            'font1':  self.lbx['FONTS.LBX'].read_font(0),
            'font2':  self.lbx['FONTS.LBX'].read_font(1),
            'font3':  self.lbx['FONTS.LBX'].read_font(2),
            'font4':  self.lbx['FONTS.LBX'].read_font(3),
            'font5':  self.lbx['FONTS.LBX'].read_font(4),
            'font6':  self.lbx['FONTS.LBX'].read_font(5)
        }
# ------------------------------------------------------------------------------
    def get_font(self, font_id):
        """Returns a graphical font identified by font_id"""
        return self.fonts[font_id]
# ------------------------------------------------------------------------------
    def __load_palettes(self):
        """Loads a color palettes"""
        self.raw_palettes = {
            'FONTS_01': self.lbx['FONTS.LBX'].read_palette(1),
            'FONTS_02': self.lbx['FONTS.LBX'].read_palette(2),
            'FONTS_03': self.lbx['FONTS.LBX'].read_palette(3),
            'FONTS_04': self.lbx['FONTS.LBX'].read_palette(4),
            'FONTS_05': self.lbx['FONTS.LBX'].read_palette(5),
            'FONTS_06': self.lbx['FONTS.LBX'].read_palette(6),
            'FONTS_07': self.lbx['FONTS.LBX'].read_palette(7),
            'FONTS_08': self.lbx['FONTS.LBX'].read_palette(8),
            'FONTS_09': self.lbx['FONTS.LBX'].read_palette(9),
            'FONTS_10': self.lbx['FONTS.LBX'].read_palette(10),
            'FONTS_11': self.lbx['FONTS.LBX'].read_palette(11),
            'FONTS_12': self.lbx['FONTS.LBX'].read_palette(12),
            'FONTS_13': self.lbx['FONTS.LBX'].read_palette(13),

            'IFONTS_1': self.lbx['IFONTS.LBX'].read_palette(1),
            'IFONTS_2': self.lbx['IFONTS.LBX'].read_palette(2),
            'IFONTS_3': self.lbx['IFONTS.LBX'].read_palette(3),
            'IFONTS_4': self.lbx['IFONTS.LBX'].read_palette(4)
        }
        self.palettes = {
            'APP_PICS': copy.deepcopy(self.raw_palettes['FONTS_02']),
            'BUFFER0':  copy.deepcopy(self.raw_palettes['FONTS_02']),
            'COLBLDG':  copy.deepcopy(self.raw_palettes['FONTS_02']),
            'COLONY2':  copy.deepcopy(self.raw_palettes['FONTS_02']),
            'COLPUPS':  copy.deepcopy(self.raw_palettes['FONTS_02']),
            'COLSUM':   copy.deepcopy(self.raw_palettes['FONTS_02']),
            'COLSYSDI': copy.deepcopy(self.raw_palettes['FONTS_02']),
            'GAME':     copy.deepcopy(self.raw_palettes['FONTS_01']),
            'INFO':     copy.deepcopy(self.raw_palettes['FONTS_01']),
            'MAINMENU': copy.deepcopy(self.raw_palettes['FONTS_06']),
            'OFFICER':  copy.deepcopy(self.raw_palettes['FONTS_02']),
            'PLANETS':  copy.deepcopy(self.raw_palettes['FONTS_02']),
            'RACEICON': copy.deepcopy(self.raw_palettes['FONTS_02']),
            'SR_R9_SC': copy.deepcopy(self.raw_palettes['FONTS_02']),
            'SHIPS':    copy.deepcopy(self.raw_palettes['IFONTS_3'])
        }
# ------------------------------------------------------------------------------
    def __get_img_key(self, img_key, subkey1 = None, subkey2 = None, subkey3 = None):
        """Helper method - returns whole image key from given parts"""
        for subkey in [subkey1, subkey2, subkey3]:
            if subkey is None:
                break
            img_key += ".%s" % subkey
        ## print img_key
        return img_key
# ------------------------------------------------------------------------------
    def set_image(self, image_data, img_key, subkey1 = None, subkey2 = None, subkey3 = None):
        """Stores a given image object to image pool udner given image key"""
        self.__image_pool[self.__get_img_key(img_key, subkey1, subkey2, subkey3)] = image_data
# ------------------------------------------------------------------------------
    def get_image(self, img_key, subkey1 = None, subkey2 = None, subkey3 = None):
        """Returns an image object from image pool identified by image key"""
        full_key = self.__get_img_key(img_key, subkey1, subkey2, subkey3)
        if self.has_image(full_key):
            return self.__image_pool[full_key]
        else:
            print "ERROR: get_image(%s) failed" % full_key
            return None
# ------------------------------------------------------------------------------
    def has_image(self, img_key, subkey1 = None, subkey2 = None, subkey3 = None):
        """Returns True if image pool contains required image key"""
        return self.__image_pool.has_key(self.__get_img_key(img_key, subkey1, subkey2, subkey3))
# ------------------------------------------------------------------------------
    def __load_lbx_solid_image(self, lbx_key, picture_id, palette_key, img_key , subkey1 = None, subkey2 = None, subkey3 = None):
        """Loads an LBX image object into image pool, the image is considered as non-transparent"""
        self.set_image(self.lbx[lbx_key].get_surface(picture_id, 0, self.palettes[palette_key], None), img_key, subkey1, subkey2, subkey3)
# ------------------------------------------------------------------------------
    def __load_lbx_transparent_image(self, lbx_key, picture_id, palette_key, color_key, img_key , subkey1 = None, subkey2 = None, subkey3 = None):
        """Loads an LBX image object into image pool, transparent LBX image has once color that is considered as fully transparent"""
        self.set_image(self.lbx[lbx_key].get_surface(picture_id, 0, self.palettes[palette_key], color_key), img_key, subkey1, subkey2, subkey3)
# ------------------------------------------------------------------------------
    def get_planet_background(self, terrain_id, picture_index):
        """Returns planet background image object from image pool"""
        bg_pics = [0, 3, 6, 9, 12, 15, 18, 23, 24, 27]
        img_index = bg_pics[terrain_id] + picture_index
        if not self.has_image('background', 'planet_terrain', img_index):
            self.__load_lbx_transparent_image('PLANETS.LBX', img_index, 'PLANETS', 0x0, 'background', 'planet_terrain', img_index)
        return self.get_image('background', 'planet_terrain', img_index)
# ------------------------------------------------------------------------------
    def __load_graphic(self, graphic_ini):
        """Loads images to image pool

        graphic_ini is supposed to be a list of strings from graphic.ini (each line = one string)

        Only LBX archive images are supported now, but can be extended to support any common graphical format e.g. PNG, JPG or GIF

        """
        print "Loading graphic..."
        for line in graphic_ini:

#            if line and line[0] != "#":
#                print line
                line = line.split("=", 1)
                img_keys = line[0].strip().split(".", 3)
#                print img_keys
                subkey1 = subkey2 = subkey3 = None
                img_key = img_keys.pop(0)
                if len(img_keys):
                    subkey1 = str(img_keys.pop(0))
                if len(img_keys):
                    subkey2 = str(img_keys.pop(0))
                if len(img_keys):
                    subkey3 = str(img_keys.pop(0))
                options = line[1].split("|")
                source_file = options[0].strip()
                source_type = source_file.split(".")[-1].lower()
                # TODO: add support for non-original graphic
                if source_type == "lbx":
                    # original LBX image = source_file | source_index | palette_key | <transparent>
                    source_index = int(options[1].strip())
                    lbx_palette = options[2].strip()
                    lbx_transparent = (len(options) == 4) and (options[3].strip() == "transparent")
                    if lbx_transparent:
                        self.__load_lbx_transparent_image(source_file, source_index, lbx_palette, 0x00, img_key, subkey1, subkey2, subkey3)
                    else:
                        self.__load_lbx_solid_image(source_file, source_index, lbx_palette, img_key, subkey1, subkey2, subkey3)

        print "... Loading graphic Done"
# ------------------------------------------------------------------------------
    def __load_ships_lbx(self, color='all', file='ships_lbx.ini'):
        """Loads ships to image pool
        Either loads all ships of all colors (color=all) or only of one color.
        All ships are in ship.lbx in blocks, every color in it's own block of 50 images.
        There are  8 blocks for each color and one (400-449) that has monsters and Antarans.
        This is in a separate method because there are ~400 images in the lbx to load, too many to put into lbx.md5 file
        """
        block_length = 50 # from the ships.lbx file.
        colors=['red','yellow','green','white','blue','brown','purple','orange']

        if color == 'all':
            for j in xrange(len(colors)):
                self.__load_ships_lbx(colors[j])

        if color in colors:
            i = colors.index(color)
            offset = block_length*i
            for ii in range(50):
                idx = offset + ii
                #self.__load_lbx_transparent_image('SHIPS.LBX', idx, str(ii%17+1), 0x00, 'SHIP', i, ii)
                self.__load_lbx_transparent_image('SHIPS.LBX', idx, 'SHIPS', 0x00, 'SHIP', i, ii)
            return
        print('->loading ships...finished')
# ------------------------------------------------------------------------------
    def draw_line(self, (x1, y1), (x2, y2), color_list):
        """ Draws a line from [x1, y1] to [x2, y2] using the list of colors as pixel bitmap.
        The colors from list are used around one by one.
        If there's only one color in the list the line drawing is passed to pygame.draw_lie
        If the color list is empty, no drawing is performed

        """
        cols = len(color_list)

        if cols == 0:
            """no color, no drawing..."""
        elif cols == 1:
            """in case of 1 color line use original pygame function"""
            return pygame.draw.line(self.DISPLAY, color_list[0], (x1, y1), (x2, y2), 1)
        else:

            xx = float(x2 - x1)
            yy = float(y2 - y1)

            if xx == 0:
                xxx = 0
                yyy = 1
            elif yy == 0:
                xxx = 1
                yyy = 0
            else:
                xxx = min(abs(xx / yy), 1) * (xx / abs(xx))
                yyy = min(abs(yy / xx), 1) * (yy / abs(yy))

            pxarray = pygame.PixelArray(self.DISPLAY)

            x, y = float(x1), float(y1)

            pixel_count = int(max(abs(xx), abs(yy)))

            for i in range(pixel_count):
                pxarray[int(round(x))][int(round(y))] = color_list[i % cols]
                x += xxx
                y += yyy
        rect = pygame.Rect(x1, y1, x2, y2)
        rect.normalize()
        return rect
# ------------------------------------------------------------------------------
    def draw_image(self, img, pos, show_now=False):
        """Draws an image object on a display buffer"""
        if img:
            self.DISPLAY.blit(img, pos)
            if show_now:
                pygame.display.update()  ### JWL: May want to include the specific image rect
# ------------------------------------------------------------------------------
    def draw_image_by_key(self, img_key, pos, show_now=False):
        """Draws an image from the image pool to a display buffer on give position"""
        self.draw_image(self.get_image(img_key), pos, show_now)
# ------------------------------------------------------------------------------
    def repeat_draw(self, target_surface, x, y, source_surface, number, icon_width, break_count, area_width):
        """Helper method that provides repetitive image drawing e.g. production icons or colonist icons"""
        if number < break_count:
            xx = icon_width
        else:
            xx = int(area_width / number)
        for i in range(int(number)):
            target_surface.blit(source_surface, (x, y))
            x += xx
        return x
# ------------------------------------------------------------------------------
    def set_mouse_cursor(self, surface):
        """Sets a new mouse cursor"""
        self.mouse_cursor = surface
        self.mouse_cursor_size = surface.get_size()
# ------------------------------------------------------------------------------
    def update_mouse_pos(self, pos):
        """Invoked on every mouse move, stores a new mouse position"""
        self.mouse_pos = pos
# ------------------------------------------------------------------------------
    def highlight_triggers(self, triggers_list):
        """Highlight the screen's triggers by drawing a colored rectangle for any of them"""
        if self.b_highlight_triggers:
            for trigger in triggers_list:
                if trigger.has_key('rect'):
                    pygame.draw.rect(self.DISPLAY, 0x660000, trigger['rect'], 1)
# ------------------------------------------------------------------------------
    def run(self):
        """Main method that starts the GUI engine

        Gets the first data from game server, displays a SplashScreen
        Loads most of the graphic and runs the MainScreen

        """
        Network_Client.Client.fetch_game_data()
        Gui_MainScreen.Screen.start()
        Gui_SplashScreen.Screen.draw()
        self.__load_graphic(self.graphic_ini[1:])

        # init mouse
        self.set_mouse_cursor(self.get_image('mouse_cursor', 'default'))
        pygame.time.set_timer(REDRAW_MOUSE_EVENT, MOUSE_EVENT_TIMER)

        Gui_MainScreen.Screen.start()
        pygame.time.set_timer(ANIMATE_SCREEN_EVENT, ANIMATE_SCREEN_TIMER)
        self.run_screen(Gui_MainScreen.Screen)
# ------------------------------------------------------------------------------
    def process_screen_trigger(self, trigger, scr):
        """Processes the 'screen' action trigger

        Prepares the next screen, runs it and returns back
        Takes care about mouse curosr and triggers highlighting

        Screen switching is processed on a GUI level rather than on Screen level

        """
        print trigger
        next_screen = None

        s_screen = trigger['screen']

        if s_screen == "colonies":
            next_screen = Gui_ColoniesScreen.Screen

        elif s_screen == "planets":
            next_screen = Gui_PlanetsScreen.Screen

        elif s_screen == "leaders":
            next_screen = Gui_LeadersScreen.Screen

        elif s_screen == "info":
            next_screen = Gui_InfoScreen.Screen

        elif s_screen == "research":
            next_screen = Gui_ResearchScreen.Screen

        elif s_screen == "starsystem":
            next_screen = Gui_StarsystemScreen.Screen
            next_screen.open_star(trigger['star_id'])

        elif s_screen == "colony":
            next_screen = Gui_ColonyScreen.Screen
            next_screen.open_colony(trigger['colony_id'])

        elif s_screen == "colony_production":
            next_screen = Gui_ColonyProductionScreen.Screen
            next_screen.open_colony(trigger['colony_id'])

        elif s_screen == "fleets":
            next_screen = Gui_FleetScreen.Screen

        # prepare and run the next_screen
        if next_screen:
            next_screen.enter()
            self.run_screen(next_screen)
            # when back from new_screen, redraws the old screen and continue
            scr.draw()
            self.highlight_triggers(scr.list_triggers())
        else:
            scr.log_error("Unknown screen: %s" % trigger['screen'])

    def process_new_turn(self):
        """Processes the New Turn action

        Waits for the server data and returns back

        """
        if Network_Client.Client.next_turn():
            print("@ gui.GUI::process_new_turn()")
            while True:
                if Network_Client.Client.fetch_update_data():
                    return True
                else:
                    print("    ERROR: received None from GameClient::next_turn()")
        else:
            print("    ERROR: NEXT_TURN sent failed?")
        print("/ gui.GUI::process_new_turn()")
        return False

    def run_screen(self, scr):
        """Runs the given game Screen and takes care for any input.

        This method will draw the game Sreen while taking care for mouse cursor,
        evaluate the input events and pass them to a proper GUI or Screen methods.

        This is the most important function in GUI engine.
        Almost all Screen methods are invoked from this place

        """

        scr.reset_triggers_list()
        scr.prepare()
        scr.draw()
        self.highlight_triggers(scr.list_triggers())

        trigger = None

        drag_item = None

        while True:
            event = pygame.event.wait()

            if event.type == QUIT:
                print("QUIT!")
                break

            elif event.type == MOUSEBUTTONDOWN:
                print "event.type == MOUSEBUTTONDOWN<"
                print "    %s" % event
                if event.button == 1:
                    drag_item = scr.get_drag_item(event.pos)
                    print("drag_item = %s" % drag_item)


            elif event.type == MOUSEBUTTONUP:
                ### JWL: Beware that a planet system popup on the main screen will steal clicks from the surrounding main screen.
                ### JWL: So if the popup is showing, clicking NewTurn will not cause anything to happen...
                print "event.type == MOUSEBUTTONUP>"
                print "    %s" % event
                print "    %s" % type(event)
                if event.button == 1:
                    scr.on_mousedrop(drag_item, event.pos)
                    drag_item = None
                trigger = scr.on_mousebuttonup(event)

            elif event.type == MOUSEMOTION:
                self.update_mouse_pos(event.pos)
                if drag_item:
                    trigger = scr.on_mousedrag(drag_item, event.pos, event.rel)
                else:
                    scr.update_hover(event.pos)
                    trigger = scr.on_mousemotion(event)

            elif event.type == REDRAW_MOUSE_EVENT:
                self.flip()

            elif event.type == ANIMATE_SCREEN_EVENT:
                animate = scr.animate()
                if animate:
                    self.flip()

            elif event.type == KEYDOWN:
                trigger = scr.on_keydown(event)

            if trigger:
                print("    trigger = %s" % trigger)

                if trigger['action'] == "screen":
                    self.process_screen_trigger(trigger, scr)

                elif trigger['action'] == "newTurn":
                    # TODO: process boolean return value of process_new_turn() method
                    self.process_new_turn()
                    scr.draw()
                    me = Network_Client.Client.get_me()
                    print 'New turn ... need to do finished research/prod popups...'
                    if not me.i_research_tech_id:
                        trigger = {'action': "screen", 'screen': "research", 'rect': None}
                        self.process_screen_trigger(trigger, scr)

                if trigger['action'] == "ESCAPE":
                    # processed later - can be chained...
                    pass

                elif trigger['action'] == "CONFIRM":
                    # processed later - can be chained...
                    pass

                else:
                    # some screens may return a new trigger, e.g. ESCAPE
                    trigger = scr.process_trigger(trigger)

                if trigger:
                    if trigger['action'] == "CONFIRM":
                        """ Let the screen confirm the changes """
                        scr.leave_confirm()
                        return

                    if trigger['action'] == "ESCAPE":
                        """ Let the screen perform cleanup from changes """
                        scr.leave_cancel()
                        return

                trigger = None
# ------------------------------------------------------------------------------
