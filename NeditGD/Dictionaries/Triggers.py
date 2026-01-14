from NeditGD import Object
import NeditGD.properties as properties
from NeditGD.Dictionaries import TriggerAlias, BooleanID, IDNames
from NeditGD.Dictionaries.TriggerAlias import EASINGS, COLOR_IDS

__all__ = [
    "EASINGS",
    "COLOR_IDS",
]


class Trigger():
    def __init__(self, i, **kwargs): 
        super().__setattr__('_obj', Object(id=i))
        
    


    def __get_enum_value__(_, enum, value):
        for k, v in enum.items():
            if v == value:
                return k
        return None

    def __get_one_two_value__(_, value):
        vals = TriggerAlias.ONE_TWO_VALS.get(_.id, ())
        if 1 <= value <= len(vals):
            return vals[value-1]
        return None

    def __one_two_lock__(_, value):
        match value:
            case bool():
                return 1 #N/A
            case int():
                if value < 1 or value > 2:
                    return 1
                else:
                    return value
            case str():
                if value.lower() in ['x', 'lock_x', 'x_lock', '1']:
                        return 1
                if value.lower() in ['y', 'lock_y', 'y_lock', '2']:
                        return 2
            case _:
                return 1

    def __convert_from_bool__(_, value):
        match value:
            case int():
                if value in [0, 1]:
                    return True if 1 else False
                else:
                    return False
            case bool():
                return value
            case str():
                if value.lower() in ['true', 't', '1']:
                    return True
                else:
                    return False
        return value

        
    
    def __convert_to_bool__(_, value):
        match value:
            case bool():
                return 1 if True else 0
            case int():
                if value < 0 or value > 1:
                    return 0
                else:
                    return value
            case str():
                if value.lower() in ['1', 'true', 't']:
                    return 1
                else:
                    return 0
            case _:
                return 0
        


    def __str__(self, custom_keys = {}):
        descr = ''
        
        for k, v in self._obj.data.items():
            if Object.is_tmp_key(k):
    
                key_str = k
            else:
                key_str = properties.get_property_name(k)

            if len(custom_keys) > 0:
                if key_str in custom_keys.keys():
                        key_str = custom_keys[key_str]

            if key_str.startswith('_'): continue

            xtra = ''
            if self.id in IDNames.OBJECT_IDS.values() and k == 1:
                for key, val in IDNames.OBJECT_IDS.items():
                    if self.id == val:
                        xtra = f'({key})'
            
            if k == 1:
                descr += f'{key_str}={v}{xtra}, '
                        

            elif self.id in TriggerAlias.ONE_TWO_VALS.keys() and (type(v) is int and k in IDNames.ONE_TWO_KEYS):
                descr += f'{key_str}={self.__get_one_two_value__(v)}, '

            elif type(v) is int and k in BooleanID.BOOLEAN_IDS:
                descr += f'{key_str}={bool(v)}, '

            elif type(v) is str:
                descr += f'{key_str}=\"{v}\", '

            else:
                descr += f'{key_str}={v}, '

        descr = f'{type(self).__name__}({descr[:-2]})'
        return descr
        
          
    def __getattr__(self, name):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.TRIGGER['id']:
                return getattr(self._obj, TriggerAlias.TRIGGER['id'][0])

            case _ if name.lower() in TriggerAlias.TRIGGER['touch']:
                return getattr(self._obj, TriggerAlias.TRIGGER['touch'][0])

            case _ if name.lower() in TriggerAlias.TRIGGER['spawn']:
                return getattr(self._obj, TriggerAlias.TRIGGER['spawn'][0])

            case _:
                return getattr(self._obj, name)
        
        
    def __setattr__(self, name, value):
        if name == "_obj":
            super().__setattr__(name, value)
            return
        else:
            match (name.lower()):
                case _ if name.lower() in TriggerAlias.TRIGGER['id']:
                    pass #cannot modify id

                case _ if name.lower() in TriggerAlias.TRIGGER['touch']:
                    setattr(self._obj, TriggerAlias.TRIGGER['touch'][0], value)

                case _ if name.lower() in TriggerAlias.TRIGGER['spawn']:
                    setattr(self._obj, TriggerAlias.TRIGGER['spawn'][0], value)

                case _:
                    setattr(self._obj, name, value)

    


class StartPos(Trigger):
    def __init__(self, **kwargs):
        super().__init__(31)
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        return super().__str__({
            TriggerAlias.STARTPOS['gamemode'][0]: 'gamemode',
            TriggerAlias.STARTPOS['speed'][0]: 'speed',
            TriggerAlias.STARTPOS['reset'][0]: 'reset',
            TriggerAlias.STARTPOS['disable'][0]: 'disable',
            TriggerAlias.STARTPOS['target_order'][0]: 'target_order',
            TriggerAlias.STARTPOS['target_channel'][0]: 'target_channel',
            TriggerAlias.STARTPOS['mnm'][0]: 'mini_mode',
            TriggerAlias.STARTPOS['mrm'][0]: 'mirror_mode',
            TriggerAlias.STARTPOS['rotg'][0]: 'rotate_gameplay',
            TriggerAlias.STARTPOS['dm'][0]: 'dual_mode',
            TriggerAlias.STARTPOS['fg'][0]: 'flip_gravity',
            TriggerAlias.STARTPOS['revg'][0]: 'reverse_gameplay'
        })
    

    def __getattr__(self, name):
        match(name.lower()):
            case _ if name.lower() in TriggerAlias.STARTPOS['gamemode']:
                return getattr(self._obj, TriggerAlias.STARTPOS['gamemode'][0])

            case _ if name.lower() in TriggerAlias.STARTPOS['speed']:
                return getattr(self._obj, TriggerAlias.STARTPOS['speed'][0])

            case _ if name.lower() in TriggerAlias.STARTPOS['reset']:
                return getattr(self._obj, TriggerAlias.STARTPOS['reset'][0])

            case _ if name.lower() in TriggerAlias.STARTPOS['disable']:
                return getattr(self._obj, TriggerAlias.STARTPOS['disable'][0])

            case _ if name.lower() in TriggerAlias.STARTPOS['target_order']:
                return getattr(self._obj, TriggerAlias.STARTPOS['target_order'][0])

            case _ if name.lower() in TriggerAlias.STARTPOS['target_channel']:
                return getattr(self._obj, TriggerAlias.STARTPOS['target_channel'][0])

            case _ if name.lower() in TriggerAlias.STARTPOS['mnm']:
                return getattr(self._obj, TriggerAlias.STARTPOS['mnm'][0])

            case _ if name.lower() in TriggerAlias.STARTPOS['mrm']:
                return getattr(self._obj, TriggerAlias.STARTPOS['mrm'][0])
            
            case _ if name.lower() in TriggerAlias.STARTPOS['rotg']:
                return getattr(self._obj, TriggerAlias.STARTPOS['rotg'][0])
            
            case _ if name.lower() in TriggerAlias.STARTPOS['dm']:
                return getattr(self._obj, TriggerAlias.STARTPOS['dm'][0])
            
            case _ if name.lower() in TriggerAlias.STARTPOS['fg']:
                return getattr(self._obj, TriggerAlias.STARTPOS['fg'][0])
            
            case _ if name.lower() in TriggerAlias.STARTPOS['revg']:
                return getattr(self._obj, TriggerAlias.STARTPOS['revg'][0])

            
            case _:
                return super().__getattr__(name)
            
    
    def __setattr__(self, name, value):
        match(name.lower()):
            case _ if name.lower() in TriggerAlias.STARTPOS['gamemode']:
                setattr(self._obj, TriggerAlias.STARTPOS['gamemode'][0], value)

            case _ if name.lower() in TriggerAlias.STARTPOS['speed']:
                setattr(self._obj, TriggerAlias.STARTPOS['speed'][0], value)

            case _ if name.lower() in TriggerAlias.STARTPOS['reset']:
                setattr(self._obj, TriggerAlias.STARTPOS['reset'][0], value)

            case _ if name.lower() in TriggerAlias.STARTPOS['disable']:
                setattr(self._obj, TriggerAlias.STARTPOS['disable'][0], value)

            case _ if name.lower() in TriggerAlias.STARTPOS['target_order']:
                setattr(self._obj, TriggerAlias.STARTPOS['target_order'][0], value)

            case _ if name.lower() in TriggerAlias.STARTPOS['target_channel']:
                setattr(self._obj, TriggerAlias.STARTPOS['target_channel'][0], value)

            case _ if name.lower() in TriggerAlias.STARTPOS['mnm']:
                setattr(self._obj, TriggerAlias.STARTPOS['mnm'][0], value)

            case _ if name.lower() in TriggerAlias.STARTPOS['mrm']:
                setattr(self._obj, TriggerAlias.STARTPOS['mrm'][0], value)
            
            case _ if name.lower() in TriggerAlias.STARTPOS['rotg']:
                setattr(self._obj, TriggerAlias.STARTPOS['rotg'][0], value)
            
            case _ if name.lower() in TriggerAlias.STARTPOS['dm']:
                setattr(self._obj, TriggerAlias.STARTPOS['dm'][0], value)
            
            case _ if name.lower() in TriggerAlias.STARTPOS['fg']:
                setattr(self._obj, TriggerAlias.STARTPOS['fg'][0], value)
            
            case _ if name.lower() in TriggerAlias.STARTPOS['revg']:
                setattr(self._obj, TriggerAlias.STARTPOS['revg'][0], value)
                
            
            case _:
                super().__setattr__(name, value)



class Color(Trigger): 
    def __init__(self, **kwargs):
        super().__init__(899)
        for key, value in kwargs.items():
            setattr(self, key, value)

    
    def __str__(self):
        return super().__str__({
            TriggerAlias.COLOR['fade_time'][0]: 'fade_time',
            TriggerAlias.COLOR['red'][0]: 'red',
            TriggerAlias.COLOR['green'][0]: 'green',
            TriggerAlias.COLOR['blue'][0]: 'blue',
            TriggerAlias.COLOR['target'][0]: 'target',
            TriggerAlias.COLOR['blending'][0]: 'blending',
            TriggerAlias.COLOR['copy_color'][0]: 'copy_color',
            TriggerAlias.COLOR['copy_color_hsv'][0]: 'copy_color_hsv',
            TriggerAlias.COLOR['copy_opacity'][0]: 'copy_opacity',
            TriggerAlias.COLOR['legacy_hsv'][0]: 'legacy_hsv',
            TriggerAlias.COLOR['player_color_1'][0]: 'player_color_1',
            TriggerAlias.COLOR['player_color_2'][0]: 'player_color_2'
        })
    
    
    def __getattr__(self, name):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.COLOR['fade_time']:
                return getattr(self._obj, TriggerAlias.COLOR['fade_time'][0])

            case _ if name.lower() in TriggerAlias.COLOR['red']:
                return getattr(self._obj, TriggerAlias.COLOR['red'][0])

            case _ if name.lower() in TriggerAlias.COLOR['green']:
                return getattr(self._obj, TriggerAlias.COLOR['green'][0])

            case _ if name.lower() in TriggerAlias.COLOR['blue']:
                return getattr(self._obj, TriggerAlias.COLOR['blue'][0])
            
            case _ if name.lower() in TriggerAlias.COLOR['target']: #special ids
                return super().__get_enum_value__(TriggerAlias.COLOR_IDS, getattr(self._obj, TriggerAlias.COLOR['target'][0]))
            
            case _ if name.lower() in TriggerAlias.COLOR['blending']:
                return getattr(self._obj, TriggerAlias.COLOR['blending'][0])
            
            case _ if name.lower() in TriggerAlias.COLOR['copy_color']:#special ids
                return super().__get_enum_value__(TriggerAlias.COLOR_IDS, getattr(self._obj, TriggerAlias.COLOR['copy_color'][0]))
            
            case _ if name.lower() in TriggerAlias.COLOR['copy_color_hsv']:
                return getattr(self._obj, TriggerAlias.COLOR['copy_color_hsv'][0])
            
            case _ if name.lower() in TriggerAlias.COLOR['copy_opacity']:
                return getattr(self._obj, TriggerAlias.COLOR['copy_opacity'][0])

            case _ if name.lower() in TriggerAlias.COLOR['legacy_hsv']: #boolean value flipped for some reason
                return super().__convert_from_bool__(not getattr(self._obj, TriggerAlias.COLOR['legacy_hsv'][0]))
            
            case _ if name.lower() in TriggerAlias.COLOR['player_color_1']:
                return getattr(self._obj, TriggerAlias.COLOR['player_color_1'][0])
            
            case _ if name.lower() in TriggerAlias.COLOR['player_color_2']:
                return getattr(self._obj, TriggerAlias.COLOR['player_color_2'][0])

            case _:
                return super().__getattr__(name)

    
    def __setattr__(self, name, value):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.COLOR['fade_time']:
                setattr(self._obj, TriggerAlias.COLOR['fade_time'][0], value)

            case _ if name.lower() in TriggerAlias.COLOR['red']:
                setattr(self._obj, TriggerAlias.COLOR['red'][0], value)

            case _ if name.lower() in TriggerAlias.COLOR['green']:
                setattr(self._obj, TriggerAlias.COLOR['green'][0], value)

            case _ if name.lower() in TriggerAlias.COLOR['blue']:
                setattr(self._obj, TriggerAlias.COLOR['blue'][0], value)
            
            case _ if name.lower() in TriggerAlias.COLOR['target']: #special ids
                if (value in TriggerAlias.COLOR_IDS.keys()):
                    value = TriggerAlias.COLOR_IDS[value]
                setattr(self._obj, TriggerAlias.COLOR['target'][0], value)
            
            case _ if name.lower() in TriggerAlias.COLOR['blending']:
                setattr(self._obj, TriggerAlias.COLOR['blending'][0], value)
            
            case _ if name.lower() in TriggerAlias.COLOR['copy_color']: #special ids
                setattr(self._obj, TriggerAlias.COLOR['copy_color'][0], value)
                
                setattr(self._obj, TriggerAlias.COLOR['copy_color'][0], value)
            
            case _ if name.lower() in TriggerAlias.COLOR['copy_color_hsv']:
                setattr(self._obj, TriggerAlias.COLOR['copy_color_hsv'][0], value)
            
            case _ if name.lower() in TriggerAlias.COLOR['copy_opacity']:
                setattr(self._obj, TriggerAlias.COLOR['copy_opacity'][0], value)

            case _ if name.lower() in TriggerAlias.COLOR['legacy_hsv']: #boolean value flipped for some reason
                value = super().__convert_to_bool__(not value)
                setattr(self._obj, TriggerAlias.COLOR['legacy_hsv'][0], value)
            
            case _ if name.lower() in TriggerAlias.COLOR['player_color_1']:
                setattr(self._obj, TriggerAlias.COLOR['player_color_1'][0], value)
            
            case _ if name.lower() in TriggerAlias.COLOR['player_color_2']:
                setattr(self._obj, TriggerAlias.COLOR['player_color_2'][0], value)

            case _:
                super().__setattr__(name, value)


class Move(Trigger):
    def __init__(self, **kwargs):
        super().__init__(901)
        for key, value in kwargs.items():
            setattr(self, key, value)

    
    def __str__(self):
        return super().__str__({
            TriggerAlias.MOVE['target'][0]: 'target',
            TriggerAlias.MOVE['move_x'][0]: 'move_x',
            TriggerAlias.MOVE['move_y'][0]: 'move_y',
            TriggerAlias.MOVE['duration'][0]: 'duration',
            TriggerAlias.MOVE['player_x_lock'][0]: 'player_x_lock',
            TriggerAlias.MOVE['player_y_lock'][0]: 'player_y_lock',
            TriggerAlias.MOVE['mod_x'][0]: 'mod_x',
            TriggerAlias.MOVE['mod_y'][0]: 'mod_y',
            TriggerAlias.MOVE['camera_lock_x'][0]: 'camera_lock_x',
            TriggerAlias.MOVE['camera_lock_y'][0]: 'camera_lock_y',
            TriggerAlias.MOVE['target_mode'][0]: 'use_target',
            TriggerAlias.MOVE['lock_xy'][0]: 'lock_xy',
            TriggerAlias.MOVE['target_p1'][0]: 'target_p1',
            TriggerAlias.MOVE['target_p2'][0]: 'target_p2',
            TriggerAlias.MOVE['target_group'][0]: 'target_group',
            TriggerAlias.MOVE['center_group'][0]: 'center_group',
            TriggerAlias.MOVE['direction_mode'][0]: 'direction_mode',
            TriggerAlias.MOVE['direction_distance'][0]: 'direction_distance',
            TriggerAlias.MOVE['small_step'][0]: 'small_step',
            TriggerAlias.MOVE['dynamic_mode'][0]: 'dynamic_mode',
            TriggerAlias.MOVE['silent'][0]: 'silent',
            TriggerAlias.MOVE['easing'][0]: 'easing',
            TriggerAlias.MOVE['easing_rate'][0]: 'easing_rate'
        })
    
    
    def __getattr__(self, name):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.MOVE['target']:
                return getattr(self._obj, TriggerAlias.MOVE['target'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['move_x']:
                return getattr(self._obj, TriggerAlias.MOVE['move_x'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['move_y']:
                return getattr(self._obj, TriggerAlias.MOVE['move_y'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['duration']:
                return getattr(self._obj, TriggerAlias.MOVE['duration'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['player_x_lock']:
                return getattr(self._obj, TriggerAlias.MOVE['player_x_lock'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['player_y_lock']:
                return getattr(self._obj, TriggerAlias.MOVE['player_y_lock'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['mod_x']:
                return getattr(self._obj, TriggerAlias.MOVE['mod_x'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['mod_y']:
                return getattr(self._obj, TriggerAlias.MOVE['mod_y'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['camera_lock_x']:
                return getattr(self._obj, TriggerAlias.MOVE['camera_lock_x'][0])
                
            case _ if name.lower() in TriggerAlias.MOVE['camera_lock_y']:
                return getattr(self._obj, TriggerAlias.MOVE['camera_lock_y'][0])
                
            case _ if name.lower() in TriggerAlias.MOVE['target_mode']:
                return getattr(self._obj, TriggerAlias.MOVE['target_mode'][0])
                
            case _ if name.lower() in TriggerAlias.MOVE['lock_xy']: #cap 1-2
                return getattr(self._obj, TriggerAlias.MOVE['lock_xy'][0])
                
            case _ if name.lower() in TriggerAlias.MOVE['target_p1']:
                return getattr(self._obj, TriggerAlias.MOVE['target_p1'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['target_p2']:
                return getattr(self._obj, TriggerAlias.MOVE['target_p2'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['target_group']:
                return getattr(self._obj, TriggerAlias.MOVE['target_group'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['center_group']:
                return getattr(self._obj, TriggerAlias.MOVE['center_group'][0])

            case _ if name.lower() in TriggerAlias.MOVE['direction_mode']:
                return getattr(self._obj, TriggerAlias.MOVE['direction_mode'][0])

            case _ if name.lower() in TriggerAlias.MOVE['direction_distance']:
                return getattr(self._obj, TriggerAlias.MOVE['direction_distance'][0])

            case _ if name.lower() in TriggerAlias.MOVE['small_step']:
                return getattr(self._obj, TriggerAlias.MOVE['small_step'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['dynamic_mode']:
                return getattr(self._obj, TriggerAlias.MOVE['dynamic_mode'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['silent']:
                return getattr(self._obj, TriggerAlias.MOVE['silent'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['small_step']:
                return getattr(self._obj, TriggerAlias.MOVE['small_step'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['easing']:
                return getattr(self._obj, TriggerAlias.MOVE['easing'][0])
            
            case _ if name.lower() in TriggerAlias.MOVE['easing_rate']:
                return getattr(self._obj, TriggerAlias.MOVE['easing_rate'][0])

            case _:
                return super().__getattr__(name)

    
    def __setattr__(self, name, value):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.MOVE['target']:
                setattr(self._obj, TriggerAlias.MOVE['target'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['move_x']:
                setattr(self._obj, TriggerAlias.MOVE['move_x'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['move_y']:
                setattr(self._obj, TriggerAlias.MOVE['move_y'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['duration']:
                setattr(self._obj, TriggerAlias.MOVE['duration'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['player_x_lock']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['player_x_lock'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['player_y_lock']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['player_y_lock'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['mod_x']:
                setattr(self._obj, TriggerAlias.MOVE['mod_x'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['mod_y']:
                setattr(self._obj, TriggerAlias.MOVE['mod_y'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['camera_lock_x']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['camera_lock_x'][0], value)
                
            case _ if name.lower() in TriggerAlias.MOVE['camera_lock_y']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['camera_lock_y'][0], value)
                
            case _ if name.lower() in TriggerAlias.MOVE['target_mode']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['target_mode'][0], value)
                
            case _ if name.lower() in TriggerAlias.MOVE['lock_xy']: 
                value = super().__one_two_lock__(value) #cap 1-2
                setattr(self._obj, TriggerAlias.MOVE['lock_xy'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['target_p1']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['target_p1'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['target_p2']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['target_p2'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['target_group']:
                setattr(self._obj, TriggerAlias.MOVE['target_group'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['center_group']:
                setattr(self._obj, TriggerAlias.MOVE['center_group'][0], value)

            case _ if name.lower() in TriggerAlias.MOVE['direction_mode']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['direction_mode'][0], value)

            case _ if name.lower() in TriggerAlias.MOVE['direction_distance']:
                setattr(self._obj, TriggerAlias.MOVE['direction_distance'][0], value)

            case _ if name.lower() in TriggerAlias.MOVE['small_step']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['small_step'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['dynamic_mode']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['dynamic_mode'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['silent']:               
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['silent'][0], value)       
            
            case _ if name.lower() in TriggerAlias.MOVE['small_step']:
                value = super().__convert_to_bool__(value)
                setattr(self._obj, TriggerAlias.MOVE['small_step'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['easing']:
                if not value >= 0 and value <= 18:
                    value = 0
                setattr(self._obj, TriggerAlias.MOVE['easing'][0], value)
            
            case _ if name.lower() in TriggerAlias.MOVE['easing_rate']:
                if value >= 1 and value <= 6:   
                    setattr(self._obj, TriggerAlias.MOVE['easing_rate'][0], value)  

            case _:
                super().__setattr__(name, value)


class Stop(Trigger):
    def __init__(self, **kwargs):
        super().__init__(1616)
        for key, value in kwargs.items():
            setattr(self, key, value)
    
        
    def __str__(self):
        return super().__str__({
            TriggerAlias.STOP['target'][0]: 'target',
            TriggerAlias.STOP['status'][0]: 'pause_resume',
            TriggerAlias.STOP['use_control_id'][0]: 'use_control_id'
        })
    
        
    def __getattr__(self, name):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.STOP['target']:
                return getattr(self._obj, TriggerAlias.STOP['target'][0])
            
            case _ if name.lower() in TriggerAlias.STOP['status']:
                return getattr(self._obj, TriggerAlias.STOP['status'][0])
            
            case _ if name.lower() in TriggerAlias.STOP['use_control_id']:
                return getattr(self._obj, TriggerAlias.STOP['use_control_id'][0])

            case _:
                return super().__getattr__(name)
    
                
    def __setattr__(self, name, value):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.STOP['target']:
                setattr(self._obj, TriggerAlias.STOP['target'][0], value)
            
            case _ if name.lower() == 'pause':
                setattr(self._obj, TriggerAlias.STOP['status'][0], 1)

            case _ if name.lower() == 'resume':
                setattr(self._obj, TriggerAlias.STOP['status'][0], 2)

            case _ if name.lower() in TriggerAlias.STOP['status']:
                value = super().__one_two_lock__(value)
                setattr(self._obj, TriggerAlias.STOP['status'][0], value)

            case _ if name.lower() in TriggerAlias.STOP['use_control_id']:
                setattr(self._obj, TriggerAlias.STOP['use_control_id'][0], value)

            case _:
                super().__setattr__(name, value)
    
        


            





class Random(Trigger):
    def __init__(self, **kwargs):
        super().__init__(1912)
        for key, value in kwargs.items():
            setattr(self, key, value)

    
    def __str__(self):
        return super().__str__({
            TriggerAlias.RANDOM['chance'][0]: 'chance',
            TriggerAlias.RANDOM['g1'][0]: 'group_1',
            TriggerAlias.RANDOM['g2'][0]: 'group_2'
        })
        
         
    def __getattr__(self, name):
        match(name.lower()):
            case _ if name.lower() in TriggerAlias.RANDOM['chance']:
                return getattr(self._obj, TriggerAlias.RANDOM['chance'][0])

            case _ if name.lower() in TriggerAlias.RANDOM['g1']:
                return getattr(self._obj, TriggerAlias.RANDOM['g1'][0])

            case _ if name.lower() in TriggerAlias.RANDOM['g2']:
                return getattr(self._obj, TriggerAlias.RANDOM['g2'][0])


            case _:
                return super().__getattr__(name)
    

    def __setattr__(self, name, value):
        match(name.lower()):
            case _ if name.lower() in TriggerAlias.RANDOM['chance']:
                setattr(self._obj, TriggerAlias.RANDOM['chance'][0], value)

            case _ if name.lower() in TriggerAlias.RANDOM['g1']:
                setattr(self._obj, TriggerAlias.RANDOM['g1'][0], value)

            case _ if name.lower() in TriggerAlias.RANDOM['g2']:
                setattr(self._obj, TriggerAlias.RANDOM['g2'][0], value)

            
            case _:
                super().__setattr__(name, value)



'''
making a trigger that inherits from Trigger:
class TriggerName(Trigger):
    def __init__(self, **kwargs):
        super().__init__(ID)
        for key, value in kwargs.items():
            setattr(self, key, value)
    
        
    def __str__(self):
        return super().__str__({
            TriggerAlias.TRIGGER_NAME['key'][0]: 'key',
        })
    
        
    def __getattr__(self, name):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.TRIGGER_NAME['key']:
                return getattr(self._obj, TriggerAlias.TRIGGER_NAME['key'][0])


            case _:
                return super().__getattr__(name)
    
                
    def __setattr__(self, name, value):
        match (name.lower()):
            case _ if name.lower() in TriggerAlias.TRIGGER_NAME['key']:
                setattr(self._obj, TriggerAlias.TRIGGER_NAME['key'][0], value)


            case _:
                super().__setattr__(name, value)



'''