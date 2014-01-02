import sys

import Game_Args
import Game_Main
import Game_Rules
import Network_Server
import openmoo2
import Data_BUILDINGS
import Data_CONST
import Data_TECH

# ------------------------------------------------------------------------------
def show_usage(name, message):
    print
    print(message)
    print("Usage:")
    print("	%s -g <savegame> [-h listen host] [-p listen port]" % name)
    print
# ------------------------------------------------------------------------------
def main(argv):
    default_options = {
        '-g':   "SAVE1.GAM",
        '-h':	"localhost",
        '-p':	9999,
    }

    (OPTIONS, PARAMS) = Game_Args.parse_cli_args(argv, default_options)

    LISTEN_ADDR = OPTIONS['-h']
    LISTEN_PORT = OPTIONS['-p']
    GAME_FILE	= OPTIONS['-g']

    if GAME_FILE == '':
        show_usage(argv[0], "ERROR: Missing game file to load")
        sys.exit(1)

    print("* Init...")
    GAME = Game_Main.Game_Main(Game_Rules.DEFAULT_RULES)

    moo2_dir = openmoo2.find_moo2_dir()
    if moo2_dir is None:
        print "Error: MOO2 Game directory not found in ../, ../../ or ../../../"
        sys.exit(1)

    print("* Loading savegame from '%s/%s'" % (moo2_dir, GAME_FILE))

    Data_BUILDINGS.regularize_building_keys()
    Data_CONST.regularize_government_keys()
    Data_TECH.regularize_tech_keys()

    GAME.load_moo2_savegame(moo2_dir + "/" + GAME_FILE)
    GAME.show_stars()
    GAME.show_planets()
    GAME.show_players()
    GAME.show_colonies()
    GAME.show_ships()

    SERVER = Network_Server.Network_Server(LISTEN_ADDR, LISTEN_PORT, GAME)
    SERVER.s_name = GAME_FILE.split("/")[-1]

    print("* Run...")
    SERVER.run()

    print("* Exit...")
    sys.exit(0)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv)
