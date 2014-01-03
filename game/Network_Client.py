import socket
import pickle
import Network_GameSocket
import re
import time

class Network_Client(object):

    def __init__(self):
        self.socket = Network_GameSocket.Network_GameSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        self.socket.settimeout(1)

    def connect(self, host, port, buffer_size = 4096):
        self.socket.buffer_size = buffer_size
        self.host = host
        self.port = port
        self.socket.connect((host, port))

    def disconnect(self):
        self.socket.close()

    def recv(self):
        return self.socket.recv()

    def send(self, action, params = None):
        print("\n* ACTION: %s\nPARAMS: %s\n" % (action, str(params)))
        self.socket.send({'action': action, 'params': params})

    def login(self, player_id):
        self.player_id = int(player_id)
        self.send("LOGIN", {'player_id': player_id})

    def logout(self):
        self.send("LOGOUT")

    def get_server_name(self):
        self.send("GET_NAME")
        return self.recv()

    def fetch_colony_prod_summary(self, i_colony_id):
        o_colony = self.game_data['colonies'][i_colony_id]
        if self.player_id == o_colony.i_owner_id:
            self.send("FETCH_COLONY_PROD_SUMMARY", {'colony_id': i_colony_id})
            update_data = self.recv()
            if update_data:
                o_colony.unserialize(update_data)

    def fetch_colony_data(self):
        ok = True
        for i_colony_id, o_colony in self.game_data['colonies'].items():
            if o_colony.i_owner_id == self.player_id:
                self.send("FETCH_COLONY_DATA", {'colony_id': o_colony.i_colony_id})
                update_data = self.recv()
                if update_data:
                    o_colony.unserialize(update_data)
                    #print o_colony.serialize()
                else:
                    print("! ERROR: Network_Client::fetch_colony_data() ... no data???")
                    ok = False
        print ("fetch_colony_data DONE.")
        return ok


    def fetch_update_data(self):
        self.send("FETCH_UPDATE_DATA")
        update_data = self.recv()
        if not update_data:
            print("! ERROR: Network_Client::fetch_update_data() ... no data???")
            return False
        player = self.game_data['players'][self.player_id]
        player.unserialize(update_data)
        print ("fetch_update_data DONE.")
        self.fetch_colony_data()
        return True

    def fetch_game_data(self):
        self.send("FETCH_GAME_DATA")
        self.game_data = self.recv()
        if not self.game_data:
            print("! ERROR: Network_Client::fetch_game_data() ... no data???")
            return False
        print type(self.game_data['me'])
        print self.game_data['me'].i_player_id
        return True

    def game_data(self):
        return self.game_data

    def rules(self):
        return self.game_data['rules']

    def get_galaxy(self):
        return self.game_data['galaxy']

    def get_stardate(self):
        return self.game_data['galaxy']['stardate']

    def list_stars(self):
        return self.game_data['stars']

    def get_star(self, star_id):
        return self.game_data['stars'][star_id]

    def list_stars_by_coords(self):
        return self.game_data['stars_by_coords']

    def list_planets(self):
        return self.game_data['planets']

    def get_planet(self, planet_id):
        return self.game_data['planets'][planet_id]

    def list_colonies(self):
        return self.game_data['colonies']

    def get_colony(self, colony_id):
        return self.game_data['colonies'][colony_id]

    def list_ship_ids(self):
        """returns all ships as a list of ship_id's (old method)"""
        return self.game_data['ships']

    def list_ships(self, i_player_id=-1):
        """
        returns ships of one player as a list of starship objects
        """
        v_ships = []
        for i_ship_id, o_ship in self.game_data['ships'].items():
            o_player = self.game_data['players'][o_ship.i_owner_id]
            if o_ship.has_no_image() and hasattr(o_player, 'color'):
                o_ship.determine_image_keys(player.i_color)
            if o_ship.i_owner_id == i_player_id and o_ship.exists():
                v_ships.append(o_ship)
        return v_ships

    def list_prototypes(self):
        return self.game_data['prototypes']

    def list_officers(self):
        return self.game_data['officers']

    def list_governors(self):
        return self.game_data['governors']

    def list_players(self):
        return self.game_data['players']

    def get_player(self, player_id):
        return self.game_data['players'][player_id]

    def get_me(self):
        return self.game_data['me']

    def next_turn(self):
        print("Network_Client::next_turn()")
        self.send("NEXT_TURN")
        response = ''
# JWL: Need a timeout
        while response != 'NEXT_TURN_ACK':
            response = self.recv()
            print 'wait_for_next_turn: response = '
            print response
        return response == 'NEXT_TURN_ACK'

    def set_research(self, i_tech_id):
        self.send("SET_RESEARCH", {'tech_id': i_tech_id})
        return self.fetch_update_data()

    def get_server_status(self):
        self.send("GET_SERVER_STATUS")
        return self.recv()

    def ping(self):
        tm1 = time.time()
        self.send("PING")
        ping_response = self.recv()
        tm2 = time.time()
        ping_time = round(tm2 - tm1, 2)
        if ping_response == "PONG":
            print("PING: %ss" % (ping_time))
        else:
            print("PING: WRONG RESPONSE '%s' returned in %ss" % (ping_response, ping_time))


    def set_colony_build_queue(self, colony_id, build_queue):
        """ Sends the new build queue for given player's colony """
        self.send("SET_BUILD_QUEUE", {'colony_id': colony_id, 'build_queue': build_queue})
        #JWL# return self.fetch_game_data()
        return self.fetch_update_data()


Client = Network_Client()
