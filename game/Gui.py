import Gui_Client
import Gui_SplashScreen
import time
import pygame

# Main GUI controller object; directly referenced by the various Screen objects.
# Initialized by openmoo2.py main procedure.
GUI = Gui_Client.Gui_Client()

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    GUI.init('C:\\Work\\jwl-orion2\\moo2res')
    #GUI.run(False)
    GUI.draw_image_by_key('splash_screen', (0, 0), True)
