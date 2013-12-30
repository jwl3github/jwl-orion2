import os.path
import os
import sys
import pygame

import Game_Args
import Network_Client
import Gui
from Gui import GUI
import Data_CONST
#import autoplayer

# ------------------------------------------------------------------------------
def find_moo2_dir():

    return 'C:\\Work\\jwl-orion2\\moo2res'

    #guess_dirs = ["orion2cd", "moo2", "MOO2", "MoO2", "Moo2", "orion2", "ORION2", "Orion2", "mooii", "MOOII"]
    #for parent in range(4):
    #    p = "../" * parent
    #    for d in guess_dirs:
    #        if os.path.isdir(p + d):
    #            return p + d
# ------------------------------------------------------------------------------
def show_usage(name, message):
    print
    print(message)
    print("Usage:")
    print(" %s -player <player id> [-h listen host] [-p listen port]" % name)
    print
# ------------------------------------------------------------------------------
def main(argv):
    """
        MAIN
    """
    MOO2_DIR = find_moo2_dir()

    if not MOO2_DIR:
        print("")
        print("ERROR: no MOO2 directory found")
        print("    OpenMOO2 requires original Master of Orion 2 game data to run, see README.TXT for more information")
        print("")
        sys.exit(1)

    default_options = {
        '-h':       "localhost",
        '-p':       9999,
        '-player':  0
    }

    (OPTIONS, PARAMS) = Game_Args.parse_cli_args(argv, default_options)

    HOST               = OPTIONS['-h']
    PORT               = OPTIONS['-p']
    PLAYER_ID          = OPTIONS['-player']
    SOCKET_BUFFER_SIZE = 4096

    GUI.init(MOO2_DIR)

    pygame.mouse.set_visible(False)
    pygame.display.set_caption("OpenMOO2: PLAYER_ID = %s" % PLAYER_ID)

    Network_Client.Client.connect(HOST, PORT, SOCKET_BUFFER_SIZE)
    Network_Client.Client.login(PLAYER_ID)

#    Network_Client.Client.ping()
#    server_status = Network_Client.Client.get_server_status()
#    print("# server_status = %s" % str(server_status))


    # automation for development
#    scenario = autoplayer.AutoPlayer(CLIENT)
#    scenario.play()
#    sys.exit(0)

    #JWL#ICON = pygame.image.load(MOO2_DIR + "/orion2-icon.png")
    #JWL#pygame.display.set_icon(ICON)

    Gui.GUI.run()

    Network_Client.Client.disconnect()
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv)
