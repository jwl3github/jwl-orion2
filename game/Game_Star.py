import Game_SpaceObject

# ==============================================================================
class Game_Star(Game_SpaceObject.Game_SpaceObject):

    def __init__(self, i_star_id):
        super(Game_Star,self).__init__(i_star_id)
        self.i_star_id                      = i_star_id
        self.s_name                         = ''
        self.i_x                            = 0
        self.i_y                            = 0
        self.i_size                         = 0
        self.i_owner                        = 0
        self.i_pict_type                    = 0
        self.i_class                        = 0
        self.v_last_planet_selected         = []
        self.i_special                      = 0
        self.i_wormhole                     = 0
        self.i_blockaded_players            = 0
        self.v_blockaded_by_bitmask         = 0
        self.i_visited                      = 0
        self.i_just_visited_bitmask         = 0
        self.i_ignore_colony_ship_bitmask   = 0
        self.i_ignore_combat_bitmask        = 0
        self.i_colonize_player              = 0
        self.i_colonies_bitmask             = 0
        self.i_interdictors_bitmask         = 0
        self.i_next_wfi_in_list             = 0
        self.i_tachyon_com_bitmask          = 0
        self.i_subspace_com_bitmask         = 0
        self.i_stargates_bitmask            = 0
        self.i_jumpgates_bitmask            = 0
        self.i_artemis_bitmask              = 0
        self.i_portals_bitmask              = 0
        self.i_stagepoint_bitmask           = 0
        self.v_players_officers             = []
        self.v_object_ids                   = []
        self.v_surrender_to                 = []
        self.i_is_in_nebula                 = 0
# ------------------------------------------------------------------------------
    def construct(self, d_load_struct):
        self.i_id                           = d_load_struct['star_id']
        self.i_star_id                      = d_load_struct['star_id']
        self.s_name                         = d_load_struct['name']
        self.i_x                            = d_load_struct['x']
        self.i_y                            = d_load_struct['y']
        self.i_size                         = d_load_struct['size']
        self.i_owner                        = d_load_struct['owner']
        self.i_pict_type                    = d_load_struct['pict_type']
        self.i_class                        = d_load_struct['class']
        self.v_last_planet_selected         = d_load_struct['last_planet_selected']
        self.i_special                      = d_load_struct['special']
        self.i_wormhole                     = d_load_struct['wormhole']
        self.i_blockaded_players            = d_load_struct['blockaded_players']
        self.v_blockaded_by_bitmask         = d_load_struct['blockaded_by_bitmask']
        self.i_visited                      = d_load_struct['visited']
        self.i_just_visited_bitmask         = d_load_struct['just_visited_bitmask']
        self.i_ignore_colony_ship_bitmask   = d_load_struct['ignore_colony_ship_bitmask']
        self.i_ignore_combat_bitmask        = d_load_struct['ignore_combat_bitmask']
        self.i_colonize_player              = d_load_struct['colonize_player']
        self.i_colonies_bitmask             = d_load_struct['colonies_bitmask']
        self.i_interdictors_bitmask         = d_load_struct['interdictors_bitmask']
        self.i_next_wfi_in_list             = d_load_struct['next_wfi_in_list']
        self.i_tachyon_com_bitmask          = d_load_struct['tachyon_com_bitmask']
        self.i_subspace_com_bitmask         = d_load_struct['subspace_com_bitmask']
        self.i_stargates_bitmask            = d_load_struct['stargates_bitmask']
        self.i_jumpgates_bitmask            = d_load_struct['jumpgates_bitmask']
        self.i_artemis_bitmask              = d_load_struct['artemis_bitmask']
        self.i_portals_bitmask              = d_load_struct['portals_bitmask']
        self.i_stagepoint_bitmask           = d_load_struct['stagepoint_bitmask']
        self.v_players_officers             = d_load_struct['players_officers']
        self.v_object_ids                   = d_load_struct['object_ids']
        self.v_surrender_to                 = d_load_struct['surrender_to']
        self.i_is_in_nebula                 = d_load_struct['is_in_nebula']
# ------------------------------------------------------------------------------
    def visited(self):
        return self.i_visited != 0
# ------------------------------------------------------------------------------
    def visited_by_player(self, i_player_id):
        return (self.i_visited & (1 << i_player_id)) != 0

# ==============================================================================
class Game_UnexploredStar(Game_Star):
    def __init__(self, i_star_id, i_x, i_y, i_size, i_pict_type, i_class):
        super(Game_UnexploredStar,self).__init__(i_star_id)
        self.s_name       = 'Unexplored'
        self.i_x          = i_x
        self.i_y          = i_y
        self.i_size       = i_size
        self.i_class      = i_class
        self.i_pict_type  = i_pict_type

    def visited(self):
        return False

    def visited_by_player(self, i_player_id):
        return False

