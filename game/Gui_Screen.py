import time

import pygame
from pygame.locals import *

import Network_Client
from Data_CONST import *

MOUSE_LEFT_BUTTON       = 1
MOUSE_MIDDLE_BUTTON     = 2
MOUSE_RIGHT_BUTTON      = 3
MOUSE_WHEELUP           = 4
MOUSE_WHEELDOWN         = 5
GUI                     = None

# ==============================================================================
class Gui_Screen(object):
    """Base gui screen class.
    Every game screen class should inherit from this one.
    """
    __triggers         = []
    __old_hover        = None
    __hover            = None
    __hover_changed    = False
    __hover_mouse_pos  = None
    FONT1              = None
    FONT2              = None
    FONT3              = None
    FONT4              = None
    FONT5              = None
    FONT6              = None
    FONT_LIST          = []
    SAVED_DISPLAY_COPY = None
    PLAYER_ID          = -1

    def __init__(self):
        pass

    def init(self, GUI_):   # Called by Gui_Client::init
        global GUI
        if not GUI:
            print 'Initializing Gui_Screen...'
            GUI                  = GUI_
            Gui_Screen.FONT1     = GUI.get_font('font1')
            Gui_Screen.FONT2     = GUI.get_font('font2')
            Gui_Screen.FONT3     = GUI.get_font('font3')
            Gui_Screen.FONT4     = GUI.get_font('font4')
            Gui_Screen.FONT5     = GUI.get_font('font5')
            Gui_Screen.FONT6     = GUI.get_font('font6')
            Gui_Screen.FONT_LIST = [ None, Gui_Screen.FONT1, Gui_Screen.FONT2, Gui_Screen.FONT3, Gui_Screen.FONT4, Gui_Screen.FONT5, Gui_Screen.FONT6 ]

    def get_player_id(self):
        return Network_Client.Client.player_id

    def list_governors(self):
        return Network_Client.Client.list_governors()

    def list_officers(self):
        return Network_Client.Client.list_officers()

    def list_colonies(self):
        return Network_Client.Client.list_colonies()

    def list_players(self):
        return Network_Client.Client.list_players()

    def list_planets(self):
        return Network_Client.Client.list_planets()

    def get_stardate_text(self):
        stardate = Network_Client.Client.get_stardate()
        s = str(stardate)
        return s[:-1] + "." + s[-1]

    def get_stardate(self):
        return Network_Client.Client.get_stardate()

    def get_galaxy(self):
        return Network_Client.Client.get_galaxy()

    def get_me(self):
        return Network_Client.Client.get_me()

    def get_rules(self):
        return Network_Client.Client.rules()

    def list_ship_ids(self, i_player_id):
        return Network_Client.Client.list_ships(i_player_id)

    def list_ships(self, i_player_id):
        return Network_Client.Client.list_ships(i_player_id)

    def get_player(self, i_player_id):
        return Network_Client.Client.get_player(i_player_id)

    def get_colony(self, i_colony_id):
        return Network_Client.Client.get_colony(i_colony_id)

    def get_planet(self, i_planet_id):
        return Network_Client.Client.get_planet(i_planet_id)

    def get_star(self, i_star_id):
        return Network_Client.Client.get_star(i_star_id)

    def list_stars(self):
        return Network_Client.Client.list_stars()

    def list_stars_by_coords(self):
        return Network_Client.Client.list_stars_by_coords()

    def list_prototypes(self):
        return Network_Client.Client.list_prototypes()

    def set_research(self, i_tech_id):
        return Network_Client.Client.set_research(i_tech_id)

    def draw_line(self, color, p1, p2, line_width):
        pygame.draw.line(GUI.DISPLAY, color, p1, p2, line_width)

    def draw_rect(self, color, x, y, width, height, line_width):
        pygame.draw.rect(GUI.DISPLAY, color, pygame.Rect((x, y), (width, height)), line_width)

    def draw_image(self, t_coords, o_img):
        GUI.draw_image(o_img, t_coords)

    def draw_image_by_key(self, t_coords, s_image_name, key1=None, key2=None, key3=None):
        GUI.draw_image(GUI.get_image(s_image_name,key1,key2,key3), t_coords)

    def save_curr_display_copy(self):
        Gui_Screen.SAVED_DISPLAY_COPY = GUI.DISPLAY.copy()

    def restore_curr_display_copy(self):
        if Gui_Screen.SAVED_DISPLAY_COPY:
            GUI.DISPLAY.blit(self.SAVED_DISPLAY_COPY, (0, 0))

    def reset_curr_display_copy(self):
        Gui_Screen.SAVED_DISPLAY_COPY = None

    def get_planet_background(self, i_terrain, i_planet):
        GUI.get_planet_background(i_terrain, i_planet)

    def repeat_draw(self, x, y, source_surface, number, icon_width, break_count, area_width):
        return GUI.repeat_draw(GUI.DISPLAY, x, y, source_surface, number, icon_width, break_count, area_width)

    def fill(self, color):
        GUI.DISPLAY.fill(color)

    def run_screen(self, screen):
        GUI.run_screen(screen)

    def blit(self, item, t_coords):
        if item:
            GUI.DISPLAY.blit(item, t_coords)
        else:
            print 'Gui_Screen.blit() -- item is None'

    def blit_image(self, t_coords, img_key, subkey1 = None, subkey2 = None, subkey3 = None):
        """Returns an image object from the GUI engine, identified by its key(s)"""
        self.blit(self.get_image(img_key, subkey1, subkey2, subkey3), t_coords)

    def write_text(self, k_font, v_palette, i_x, i_y, s_text, i_letter_spacing = 1):
        Gui_Screen.FONT_LIST[k_font].write_text(GUI.DISPLAY, i_x, i_y, s_text, v_palette, i_letter_spacing)

    def render(self, k_font, v_palette, s_text, i_letter_spacing = 1):
        return Gui_Screen.FONT_LIST[k_font].render(s_text, v_palette, i_letter_spacing)

    def log_info(self, message):
        """Prints an INFO message to standard output"""
        ts = int(time.time())
        print("# INFO %i ... %s" % (ts, message))

    def log_error(self, message):
        """Prints an ERROR message to standard output"""
        ts = int(time.time())
        print("! ERROR %i ... %s" % (ts, message))

    def reset_triggers_list(self):
        """Clears the screen's trigger list"""
        self.__triggers = []

    def add_trigger(self, trigger, prepend = False):
        """Appends given trigger to the end of screen's trigger list"""
        if not trigger.has_key('hover_id'):
            trigger['hover_id'] = None
        if prepend:
            print 'Prepend trigger'
            self.__triggers.insert(0, trigger)
        else:
            self.__triggers.append(trigger)

    def list_triggers(self):
        """Returns the screen's list of triggers"""
        return self.__triggers

    def get_timestamp(self, zoom = 1):
        """Returns an actual timestamp"""
        return int(time.time() * zoom)


    def get_image(self, img_key, subkey1 = None, subkey2 = None, subkey3 = None):
        """Returns an image object from the GUI engine, identified by its key(s)"""
        return GUI.get_image(img_key, subkey1, subkey2, subkey3)


    def redraw_flip(self):
        """Redraws the screen, takes care about mouse cursor and flips the graphic buffer to display"""
        self.draw()
        GUI.highlight_triggers(self.list_triggers())
        GUI.flip()

    def redraw_noflip(self):
        """Redraws the screen, takes care about mouse cursor but doesn't flip the buffer to display"""
        self.draw()
        GUI.highlight_triggers(self.list_triggers())


    def prepare(self):
        """This method should be implemented by screens that require some
        special actions each time before the screen is run.

        For example to reset screen to a well known state to prevent unexpected behaviour.

        """
        pass

    def draw(self):
        """All static graphic output should be implemented in this method.

        Unless there is only a dynamic graphic (animations),
        every screen should implement this method.

        """
        pass

    def animate(self):
        """Entry point for Screen animations, e.g. ship trajectory on MainScreen.

        GUI engine calls this method periodically
        Animations should be time-dependant - such screens have to implement the timing!

        """
        pass


    def get_escape_trigger(self):
        """Returns standard trigger for sending escape action"""
        return {'action': "ESCAPE"}


    def on_mousebuttonup(self, event):
        """Default implementation of mouse click event serving.

        Checks the mouse wheel events (up and down scrolling) and regular mouse buttons.
        If the event's subject is the left mouse button it checks the mouse position against the trigger list and
        returns the first trigger where mouse positions is within its rectangle.

        There is a good chance that no screen would have to override this method.

        """
        if event.button == MOUSE_MIDDLE_BUTTON:
            print event

        elif event.button == MOUSE_WHEELUP:
            return {'action': "SCROLL_UP"}

        elif event.button == MOUSE_WHEELDOWN:
            return {'action': "SCROLL_DOWN"}

        else:
            triggers_list = self.list_triggers()
            for trigger in triggers_list:
                if trigger['rect'].collidepoint(event.pos):
                    if event.button == MOUSE_LEFT_BUTTON:
                        trigger['mouse_pos'] = event.pos
                        return trigger

                    elif event.button == MOUSE_RIGHT_BUTTON:
                        return {'action': "help", 'help': trigger['action']}


    def on_keydown(self, event):
        """Default implementation of a keyboard event handling.

        If keypress is detected by the GUI engine it calls this method.
        The pressed key is checked against the trigger list.
        Returns the first trigger where the key matches the pressed or
        None if no trigger matches the keypress

        There is a good chance that no screen would have to override this method.

        """
        print("@ screen.Gui_Screen::on_keydown()")
        print("    scancode = %i" % event.scancode)
        print("    key = %i" % event.key)
        if event.key == K_ESCAPE:
            return {'action': "ESCAPE"}
        else:
            triggers_list = self.list_triggers()
            for trigger in triggers_list:
                if trigger.has_key('key') and trigger['key'] == event.key:
                    return trigger
            # As a fallback for the Enter key, treat it as a left mouse click.
            # JWL: Not quite working due to key-based popups and auto-popups.
            # if event.key == 13 and self.__hover_mouse_pos:
            #     event.button = MOUSE_LEFT_BUTTON
            #     event.pos    = self.__hover_mouse_pos
            #     trigger      = self.on_mousebuttonup(event)
            #     if trigger:
            #         return trigger
            return {'action': "key", 'key': event.key}


    def update_hover(self, mouse_pos):
        """This method is invoked by the GUI engine on every pure mouse move
        and right before the screen's on_mousemotion() method.

        Mouse position is checked against screen's trigger list.
        If hover is detected (=mouse position is inside the trigger's rectangle)
        the trigger is copied and can be returned by get_hover() method

        Also if the previously stored value is different than the new one,
        the __hover_changed flag is set to True

        The idea is to handle mouse hover detection separately,
        so other methods could rely on get_hover() and hover_changed() methods.

        Probably no screen should require to override this method.

        """
        self.__hover_mouse_pos = mouse_pos
        for trigger in self.list_triggers():
            if trigger.has_key('hover_id') and trigger['rect'].collidepoint(mouse_pos):
                if self.__hover != trigger:
                    self.__hover_changed = True
                self.__hover = trigger
                break

    def get_hover(self):
        """Returns the current hover trigger"""
        return self.__hover

    def hover_changed(self):
        """Returns True if screen's hover has changed since last call of this method"""
        if self.__hover_changed:
            self.__hover_changed = False
            return True
        else:
            return False

    def on_mousemotion(self, event):
        """Invoked by the GUI engine on every pure (non-dragging) mouse move.

        Currently no screen requires to override this empty implementation.

        """
        pass

    def get_drag_item(self, mouse_pos):
        """"""
        for trigger in self.list_triggers():
            if trigger.has_key('drag_id') and trigger['rect'].collidepoint(mouse_pos):
                return trigger['drag_id']
        return None

    def on_mousedrag(self, drag_item, pos, rel):
        """Invoked by the GUI engine when left mouse button is being held, drag item is set and mouse moves"""
        pass

    def on_mousedrop(self, drag_item, (mouse_x, mouse_y)):
        """Invoked by the GUI engine when mouse dragging stops
        (drag item was set and left mouse button was released).

        """
        pass

    def process_trigger(self, trigger):
        """Empty implementation of a trigger handling

        If a screen trigger is positively evaluated
        (e.g. returned from on_mousebuttonup() or on_keydown() methods)
        it's passed as a trigger argument to this method

        Every screen should override this method to handle the proper actions.

        """
        pass

    def enter(self):
        """ Called by the GUI engine right before Gui_Client::run_screen() is invoked
        Suitable for saving initial state that can be reveresed by the screen's cancel() method

        """
        pass

    def leave_confirm(self):
        """ Called by the GUI engine when CONFIRM trigger is activated
        Every screen that sends data to the game server should implement this method

        """
        pass

    def leave_cancel(self):
        """ Called by the GUI engine when ESCAPE trigger is activated
            This is the right place to implement things like getting the screen to state before any changes were made
        """
        pass
