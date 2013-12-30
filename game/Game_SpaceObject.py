import Game_Object

class Game_SpaceObject(Game_Object.Game_Object):

    def __init__(self, obj_id):
        super(Game_SpaceObject,self).__init__(obj_id)
        self.i_x = -1
        self.i_y = -1

    def set_coords(self, i_x, i_y):
        self.i_x, self.i_y = i_x, i_y

    def get_coords(self):
        return (self.i_x, self.i_y)
