class AutoPlayer(object):

    def __init__(self, game_client):
        self.game_client = game_client

    def play(self):
        s_save_file = self.game_client.get_server_name()
        if s_save_file == 'SAVE1.GAM':
            print('AutoPlayer::play() ... starting AutoPlayer::play_SAVE1GAM()')
            self.play_SAVE1GAM()
        else:
            print('AutoPlayer::play() ... no scenario for %s' % s_save_file)

    def play_SAVE1GAM(self):
        cl = self.game_client
        cl.set_research(75)		# Galactic Currency Exchange
        cl.next_turn()
        cl.next_turn()
        cl.next_turn()
        cl.next_turn()
        cl.next_turn()
