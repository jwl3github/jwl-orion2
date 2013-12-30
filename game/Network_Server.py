import socket
import sys
import threading
import time
import hashlib
import pickle
import Network_GameSocket
import Data_CONST
from Data_CONST import *   # For K_xxx constants

# ==============================================================================
class Network_Server(object):
# ------------------------------------------------------------------------------
    def __init__(self, host, port, game):
        self.s_name               = 'unnamed'
        self.s_host               = host
        self.s_status             = 'init'
        self.i_port               = port
        self.i_socket_buffer_size = 4096
        self.r_game               = game
        self.d_players_status     = {}
        self.d_threads            = {}
        self.d_threads_next_turn  = {}

        for i_player_id in range(self.max_players()):
            self.d_players_status[i_player_id] = 0
# ------------------------------------------------------------------------------
    def spawn_server_socket(self):
        new_server_socket = Network_GameSocket.Network_GameSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        new_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #JWL# new_server_socket.settimeout(1)
        new_server_socket.setblocking(1)   # JWL: Trial with blocking sockets
        new_server_socket.settimeout(None)  # JWL: Trial with blocking sockets
        new_server_socket.bind((self.s_host, self.i_port))
        new_server_socket.listen(2)
        return new_server_socket
# ------------------------------------------------------------------------------
    def log_info(self, message):
        print("# INFO: %s" % message)

    def log_debug(self, message):
        print("> DEBUG: %s" % message)

    def log_error(self, message):
        print("! ERROR: %s" % message)
# ------------------------------------------------------------------------------
    def set_status(self, status):
        if status in ["init", "turn", "recount", "shutdown"]:
            self.s_status = status
            self.log_info("Server::set_status() ... status set to \"%s\"" % status)
        else:
            self.log_error("Server::set_status() ... bad status: %s" % status)

    def set_turn(self):
        self.set_status("turn")

    def set_recount(self):
        self.set_status("recount")

    def set_shutdown(self):
        self.set_status("shutdown")

    def check_turn(self):
        return self.s_status == "turn"

    def check_recount(self):
        return self.s_status == "recount"

    def check_shutdown(self):
        return self.s_status == "shutdown"

    def max_players(self):
        return K_MAX_PLAYERS

    def get_update_for_player(self, player_id):
        return self.r_game.get_update_for_player(player_id)

    def get_data_for_player(self, player_id):
        return self.r_game.get_data_for_player(player_id)

    def send_data_to_game_client(self, client_socket, thread_id, data):
        s = pickle.dumps(data)
#self.log_info("Server::send_data_to_game_client() ... %i bytes for thread %s" % (len(s), thread_id))
        client_socket.send(data)

    def set_next_turn(self, thread_id, player_id):
        self.d_threads_next_turn[thread_id] = player_id

    def clean_next_turn(self, thread_id):
        self.set_next_turn(thread_id, -1)

    def get_next_turn(self, thread_id):
        return self.d_threads_next_turn[thread_id]

    def wait_for_next_turn(self):
        pass
# ------------------------------------------------------------------------------
    def check_next_turn(self):
        # check_next_turn_multiplayer seems to work fine
        # but for now every game is supposed to be a single player
        return self.check_next_turn_singleplayer()
# ------------------------------------------------------------------------------
    def check_next_turn_singleplayer(self):
        # in single player human is always player_id 0
        for thread_id, player_id in self.d_threads_next_turn.items():
            if player_id == 0:
                return True
        return False
# ------------------------------------------------------------------------------
    def check_next_turn_multiplayer(self):
        pl_st = {}
        # all the clients must confirm next turn
        for thread_id, player_id in self.d_threads_next_turn.items():
            if player_id < 0:
                return False
            else:
                pl_st[player_id] = True
        self.log_info("Server::check_next_turn_multiplayer() ... pl_st = %s" % str(pl_st))
        # all players must confirm next turn
        return len(pl_st) == self.r_game.count_players()
# ------------------------------------------------------------------------------
    def handle_recv_client_data(self, player_id, client_socket, thread_id, data):
        self.log_info("data received from client # %s, player_id = %i" % (thread_id, player_id))

        ACTION = data['action']
        PARAMS = data['params']

        self.log_info("thread_id: %s\n    player_id: %i\n    ACTION: %s\n    PARAMS: %s\n" % (thread_id, player_id, ACTION, str(PARAMS)))

        if ACTION == "LOGIN":
            # SECURE ME!!!
            player_id = int(PARAMS['player_id'])
            self.log_info("thread \"%s\" ... player_id set to %i" % (thread_id, player_id ))

        elif ACTION == "LOGOUT":
            self.set_shutdown()
            return -1

        elif ACTION == "PING":
            self.send_data_to_game_client(client_socket,  thread_id, "PONG")

        elif ACTION == "GET_NAME":
            self.send_data_to_game_client(client_socket,  thread_id, self.s_name)

        elif ACTION == "GET_SERVER_STATUS":
            self.send_data_to_game_client(client_socket, thread_id, self.s_status)

        elif ACTION == "NEXT_TURN":
            self.log_info("received NEXT_TURN from thread %s ... player_id = %i" % (thread_id, player_id))
            self.set_next_turn(thread_id, player_id)
            while self.get_next_turn(thread_id) != -1:
                time.sleep(0.001)
            self.log_info("... NEXT_TURN performed, now sending NEXT_TURN_ACK")
            self.send_data_to_game_client(client_socket,  thread_id, "NEXT_TURN_ACK")

        elif player_id < 0:
            self.log_error("anonymous player sending actions!!!")

        elif ACTION == "FETCH_UPDATE_DATA":
            # JWL: Trying to separate one-time-only bulk data from dynamic updates
            # includes: 1. Database of building names/costs
            # includes: 2. Database of research names/costs
            # includes: 3. Database of hero names/attribs
            # includes: 4. Star chart with coords/colors/(names? - beware sharing Orion, unless bait-n-switch concept employed)
            data = self.get_update_for_player(player_id)
            print 'type(data) ...'
            print type(data)
            self.send_data_to_game_client(client_socket, thread_id, data)

        elif ACTION == "FETCH_GAME_DATA":
            data = self.get_data_for_player(player_id)
            self.send_data_to_game_client(client_socket, thread_id, data)

        elif ACTION == "SET_RESEARCH":
            research_item = PARAMS['tech_id']
            if not self.r_game.update_research(player_id, research_item):
                self.log_error("Game::set_research() failed ... player_id = %i, research_item = %i" % (player_id, research_item))

        elif ACTION == "SET_BUILD_QUEUE":
            if not self.r_game.set_colony_build_queue(player_id, PARAMS['colony_id'], PARAMS['build_queue']):
                self.log_error("Game::set_colony_build_queue() failed ... player_id = %i, colony_id = %i" % (player_id, PARAMS['colony_id']))

        else:
            self.log_error("unknow action received from client: '%s'" % data)

        return player_id
# ------------------------------------------------------------------------------
    def run_client_handler(self, client_socket, thread_id):
        self.log_info("thread_id: %s\n    STARTED\n" % (thread_id))
        player_id = -1
        while not self.check_shutdown():
            print 'run_client_thread %s' % str(thread_id)
            data = client_socket.recv()
            if data:
                player_id = self.handle_recv_client_data(player_id, client_socket, thread_id, data)
            else:
                break
        self.log_info("thread_id: %s\n    player_id: %i\n    CLOSING SOCKET\n" % (thread_id, player_id))
        client_socket.close()
        self.clean_next_turn(thread_id)
# ------------------------------------------------------------------------------
    def compose_thread_id(self, client_host, client_port):
        now = str(time.time())
        s = "%s:%i@%s" % (client_host, client_port, now)
        return "%s:%s:%i" % (hashlib.md5(s).hexdigest(), client_host, client_port)
# ------------------------------------------------------------------------------
    def spawn_thread(self, client_socket, client_host, client_port):
        thread_id = self.compose_thread_id(client_host, client_port)
        th = threading.Thread(target = self.run_client_handler, args=(client_socket, thread_id))
        self.log_info("Server::spawn_thread() ... new thread spawned: %s" % thread_id)
        self.d_threads_next_turn[thread_id] = -1
        self.d_threads[thread_id] = th
        self.d_threads[thread_id].setDaemon(True)
        self.d_threads[thread_id].start()
        return thread_id
# ------------------------------------------------------------------------------
    def clean_thread(self, thread_id):
        self.log_info("* Server::clean_thread() ... cleaning thread # %s" % thread_id)
        self.d_threads.pop(thread_id)
        self.d_threads_next_turn.pop(thread_id)
# ------------------------------------------------------------------------------
    def show_next_turns(self):
        for thread_id, player_id in self.d_threads_next_turn.items():
            print("? next_turn: %s ... %i" % (thread_id, player_id))
# ------------------------------------------------------------------------------
    def debug_threads(self):
        if self.d_threads:
            print("# Threads:")
            for thread_id in self.d_threads:
                is_alive = self.d_threads[thread_id].is_alive()
                self.log_debug("#    id = %s, is_alive = %i" % (thread_id, is_alive))
# ------------------------------------------------------------------------------
    def run(self):
        print('')
        print("PORT = %s" % self.i_port)
        print("SOCKET_READ_BUFFER_SIZE = " + str(self.i_socket_buffer_size))
        print("Awaiting connections...")
        print('')

        server_socket = self.spawn_server_socket()
        self.set_turn()

        while not self.check_shutdown():
            print 'run Server'
            try:
                client_socket, (client_host, client_port) = server_socket.accept()
                thread_id = self.spawn_thread(client_socket, client_host, client_port)
            except socket.timeout:
                pass

#           self.debug_threads()
#           self.show_next_turns()

            if self.d_threads:
                print 'handle_thread'
                clean_threads = []
                for thread_id in self.d_threads:
                    is_alive = self.d_threads[thread_id].is_alive()
                    if not is_alive:
                        self.log_info("Server::run() ... thread %s is not alive, will be cleaned" % thread_id)
                        clean_threads.append(thread_id)

                # clean old threads
                for thread_id in clean_threads:
                    self.clean_thread(thread_id)

                if self.check_next_turn():
                    self.log_info("got True from Server::check_next_turn() >>> DOING NEXT TURN!")
                    self.r_game.next_turn()
                    # clean next turn flags for all threads
                    for thread_id in self.d_threads:
                        self.clean_next_turn(thread_id)

        self.log_info("Closing serverSocket")
        server_socket.close()
