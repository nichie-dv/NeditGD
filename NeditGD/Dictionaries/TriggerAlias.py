from enum import IntEnum

TRIGGER = {
    'id': ['id', 'id_number', 'blockid', 'block_id'],
    'touch': ['touch_trigger', 'tt', 'touch', 'touchtrigger'],
    'spawn': ['spawn_triggered', 'st', 'spawn', 'spawntrigger', 'spawn_trigger']
}

STARTPOS = {
    'gamemode': ['gamemode', 'gm', 'game_mode', 'player_type'],
    'speed': ['sp_speed', 'speed', 'speed_type'],
    'reset': ['reset_camera', 'rc', 'reset_cam', 'resetcamera', 'resetcam'],
    'disable': ['disable', 'd', 'toggle', 'toggled', 'disabled'],
    'target_order': ['target_order', 'targetorder', 'to', 'order_target', 'ordertarget'],
    'target_channel': ['target_channel', 'targetchannel', 'tc', 'channel_target', 'channeltarget'],
    'mnm': ['mini_mode', 'mnm'],
    'mrm': ['mirror_mode', 'mrm', 'mirror'],
    'rotg': ['rotate_gameplay', 'rotg'],
    'dm': ['sp_dual_mode', 'dual_mode', 'dm', 'dual'],
    'fg': ['flip_gravity', 'fg', 'flip', 'invert_gravity'],
    'revg': ['reverse_gameplay', 'revg', 'reverse'],
}

COLOR = {
    'fade_time': ['duration', 'fade_time', 'fade', 'fadetime'],
    'red': ['trigger_red', 'red', 'r'],
    'green': ['trigger_green', 'green', 'g'],
    'blue': ['trigger_blue', 'blue', 'b'],
    'target': ['target_color', 'target', 'col'],
    'blending': ['blending', 'blend'],
    'copy_color': ['copied_color_id', 'copy_id', 'copy_color', 'cpc'],
    'copy_color_hsv': ['copied_color_hsv', 'copy_color_hsv', 'hsv'],
    'copy_opacity': ['copy_opacity', 'co', 'cpo'],
    'legacy_hsv': ['new_hsv', 'legacy_hsv', 'lhsv'],
    'player_color_1': ['player_color_1', 'pc1', 'player1'],
    'player_color_2': ['player_color_2', 'pc2', 'player2']

}

MOVE = {
    'target': ['target', 't', 'group'],
    'move_x': ['move_x', 'mvx', 'x'],
    'move_y': ['move_y', 'mvy', 'y'],
    'duration': ['duration', 'time', 'dur', 'dr'],
    'player_x_lock': ['lock_to_player_x', 'player_x_lock', 'x_lock', 'lock_x'], #boolean
    'player_y_lock': ['lock_to_player_y', 'player_y_lock', 'y_lock', 'lock_y'], #boolean
    'mod_x': ['follow_camera_x_mod', 'mdx', 'mod_x', 'camera_x_mod', 'x_mod'],
    'mod_y': ['follow_camera_y_mod', 'mdy', 'mod_y', 'camera_y_mod', 'y_mod'],
    'camera_lock_x': ['follow_camera_x', 'camera_lock_x', 'clx', 'lcx', 'lock_camera_x'], #boolean
    'camera_lock_y': ['follow_camera_y', 'camera_lock_y', 'cly', 'lcy', 'lock_camera_y'], #boolean
    'target_mode': ['use_target', 'target_mode', 'tgm'], #boolean
    'lock_xy': ['target_pos_axes', 'lock_xy', 'lock_axes'], #1(x) or 2(y)
    'target_p1': ['player_1', 'target_p1', 'pl1', 'p1'], #boolean
    'target_p2': ['player_2', 'target_p2', 'pl2', 'p2'], #boolean
    'target_group': ['target_pos', 'target_pos_group', 'target_group', 'tg'],
    'center_group': ['center_group_id', 'center_group', 'cg'],
    'direction_mode': ['follow_mode', 'direction_mode', 'dirmd', 'dir'], #boolean
    'direction_distance': ['target_move_distance', 'direction_distance', 'target_distance', 'dist', 'td'],
    'small_step': ['small_step', 'ss', 'small'], #boolean
    'dynamic_mode': ['dynamic_mode', 'dynmd', 'dymd', 'dynamic'], #boolean
    'silent': ['silent', 'silent_mode'], #boolean
    'easing': ['easing', 'ease', 'ease_type', 'easing_type'], #0-18 (use enum)
    'easing_rate': ['easing_rate', 'ease_rate', 'rate', 'er'] #only for 1-6


}

STOP = {
    'target': ['target', 't', 'group', 'target_id', 'control_target'],
    'status': ['pause_resume', 'status'], #1-2 lock
    'use_control_id': ['use_control_id', 'cid', 'control_id'] #bool
}





RANDOM = {
    'chance': ['duration', 'chance', 'random_chance', 'random_percent'],
    'g1': ['target', 'group_id_1', 'g_1', 'g1', 'group_1', 'random_g1'],
    'g2': ['target_pos', 'group_id_2', 'g_2', 'g2', 'group_2', 'random_g2'],
}


class EASINGS(IntEnum):
    NONE = 0
    EASE_IN_OUT = 1
    EASE_IN = 2
    EASE_OUT = 3
    ELASTIC_IN_OUT = 4
    ELASTIC_IN = 5
    ELASTIC_OUT = 6
    BOUNCE_IN_OUT = 7
    BOUNCE_IN = 8
    BOUNCE_OUT = 9
    EXPONENTIAL_IN_OUT = 10
    EXPONENTIAL_IN = 11
    EXPONENTIAL_OUT = 12
    SINE_IN_OUT = 13
    SINE_IN = 14
    SINE_OUT = 15
    BACK_IN_OUT = 16
    BACK_IN = 17
    BACK_OUT = 18

    
class COLOR_IDS(IntEnum):
    BG = 1000
    G1 = 1001
    LINE = 1002
    _3DL = 1003
    OBJ = 1004
    P1 = 1005
    P2 = 1006
    G2 = 1009
    MG = 1013
    MG2 = 1014



ONE_TWO_VALS = {
    901: ('lock_x', 'lock_y'),
    1616: ('pause', 'resume')
}







