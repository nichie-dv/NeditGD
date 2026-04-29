import json, sys
from NeditGD.Config import BasicConfig, LogColors
from enum import Enum

def check_data_validity(object, data):
    """
    Checks given data for faults based on object type.\n
    Does not always terminate program, but will log a warning.

    Args:
        object: Instance of data type to check
        data (any): Instance of data type to check

    Returns:
        bool: True if data is valid, otherwise False
    """

    expectation = {}
    got = {}
    fault_reason = 'unknown fault'

    fault = False
    fatal = False

    
    fault, fatal = check_format(object, data, expectation, got)
    if (fault):
        fault_reason = 'unexpected format'
    

    if (fatal):
        print(f'{LogColors.BasicColors.FAIL}[FATAL] {type(object).__name__} @ {hex(id(object))}: {fault_reason}{LogColors.BasicColors.RESET}')
        sys.exit()

    if not fault and not fatal:
        return True
    
    if BasicConfig.Config.LOG_WARNINGS:
        print(f'{LogColors.BasicColors.WARNING}[WARN] {type(object).__name__} @ {hex(id(object))}: {fault_reason}')
        print('expected:\n' + json.dumps(expectation, indent=4) + '\ngot:\n' + json.dumps(got, indent=4) + LogColors.BasicColors.RESET)

    return False


def check_format(obj, val, expectation, got) -> tuple[bool, bool]:
    """
    Checks if format of value for object is valid.

    Returns:
        tuple[bool, bool]: (Did Fault, Did Fatal Fault)
    
    """

    faulted = False
    fatal = False

    match (obj):
        case HSVString():
            char_arr = val.split('a')
            seperators = val.count('a')

            if len(char_arr) != seperators + 1:
                faulted = True

                expectation['string'] = ['0a0a0', '0a0a0a0a0']
                got['string'] = val
                

            if len(char_arr) not in (3, 5):
                faulted = True

                expectation['length'] = [3, 5]
                got['length'] = len(char_arr)
            
        
        case GroupList():
            if isinstance(val, str):
                char_arr = val.split('.')
                seperators = val.count('.')

                if len(char_arr) != seperators + 1:
                    faulted = True

                    expectation['string'] = '1.2.3.4.9999'
                    got['string'] = val
                
                for i in char_arr:
                    
                    if isinstance(i, int):
                        if i > 9999 or i < 0:
                            if (not isinstance(got['limit'], list)):
                                got['limit'] = []
                            faulted = True

                            expectation['limit'] = '0-9999'
                            got['limit'].append(i)
                    else:
                        faulted = True

                        expectation['data'] = 'int'
                        got['data'] = type(i)
                        break
            if isinstance(val, int):
                if val > 9999 or val < 0:
                    faulted = True

                    expectation['limit'] = '0-9999'
                    got['limit'] = val

        case RemapList() | AdvRandomList():
            if isinstance(val, list):
                for tup in val:
                    #invalid length of inner
                    if (len(tup) != 2):
                        if (not isinstance(got['inner_length'], list)):
                            got['inner_length'] = []
                        faulted = True

                        expectation['inner_length'] = 2
                        got['inner_length'].append(len(tup))
                    
                    #invalid characters of inner
                    if not isinstance(tup[0], int) or not isinstance(tup[1], int):
                        if (not isinstance(got['data'], list)):
                            got['data'] = []
                        faulted = True

                        expectation['data'] = 'int'
                        got['data'].append(tup)
                    #invalid groups of inner


            if isinstance(val, int):
                if val > 9999 or val < 0:
                    faulted = True

                    expectation['limit'] = '0-9999'
                    got['limit'] = val
    
    return (faulted, fatal)




    

class NInt(int):
    def __init__(self, value: int = 0):
        self._value = value

    def __str__(self):
        return self._value

    def __repr__(self):
        return self._value


class NFloat(float):
    def __init__(self, value: float = 0.0):
        self._value = value

    def __str__(self):
        return self._value

    def __repr__(self):
        return self._value


class NBool:
    def __init__(self, truth: bool = False):
        self._truth = truth

    def __str__(self):
        return self._truth

    def __repr__(self):
        return self._truth


class HSVString:
    def __init__(self, h = 0, s = 0, v = 0, s_checked = False, v_checked = False):
        self._h = h
        self._s = s
        self._v = v

        self._s_chk = s_checked
        self._v_chk = v_checked

        self._string = f'{h}a{s}a{v}a{int(s_checked)}a{int(v_checked)}'

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, val):
        self._h = max(min(val, 180), -180)
        self._update_string()

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, val):
        self._s = max(min(val, 180), -180)
        self._update_string()

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, val):
        self._v = max(min(val, 180), -180)
        self._update_string()
    

    def set(self, val: str):
        if not check_data_validity(self, val):
            return self
        self._string = val
        return self

    def _update_string(self):
        self._string = f'{self._h}a{self._s}a{self._v}a{self._s_chk}a{self._v_chk}'

    def __str__(self):
        if (self._string == ''):
            return 'None'
        return self._string

    def __repr__(self):
        if (self._string == ''):
            return 'None'
        return str(self._string)


class GroupList:
    def __init__(self, groups = None):
        self._groups = groups or []

        self._string = ''

    def _update_string(self):
        tmp = ''
        for val, index in enumerate(self._groups):
            tmp += str(val)
            if (index < len(self._groups) - 1):
                tmp += '.'
        self._string = tmp

    def set(self, val: str):
        if not check_data_validity(self, val):
            return self
        self._string = val
        return self

    @property
    def groups(self):
        return self._groups

    def __add__(self, val: int):
        if not check_data_validity(self, val):
            return self

        if (val not in self._groups):
            self._groups.append(val)

        self._update_string()
        return self

    def __sub__(self, val: int):
        if (val in self._groups):
            self._groups.remove(val)

        self._update_string()
        return self
    
    def __str__(self):
        if (self._string == ''):
            return 'None'
        return self._string

    def __repr__(self):
        if (self._string == ''):
            return 'None'
        return str(self._string)



class ParticleString:
    def __init__(self):
        #TODO: impl
        pass



class RemapList:
    def __init__(self, groups = None):
        self._groups = groups or []

        self._string = ''

    def _update_string(self):
        tmp = ''
        for index, val in enumerate(self._groups):
            tmp += (str(val[0]) + '.' + str(val[1]))
            if (index < len(self._groups) - 1):
                tmp += '.'

        self._string = tmp

    @property
    def groups(self):
        return self._groups

    def __add__(self, val: tuple | list):
        if not check_data_validity(self, val):
            return self

        if (type(val) == tuple):
            if (val not in self._groups):
                self._groups.append(val)

        if (type(val) == list):
            for entry in val:
                if (entry not in self._groups) and type(entry) == tuple:
                    self._groups.append(entry)

        self._update_string()
        return self

    def __sub__(self, val: tuple | list):
        if (type(val) == tuple):
            if (val in self._groups):
                self._groups.remove(val)

        if (type(val) == list):
            for entry in val:
                if (entry in self._groups) and type(entry) == tuple:
                    self._groups.remove(entry)

        self._update_string()
        return self
    
    def __str__(self):
        if (self._string == ''):
            return 'None'
        return self._string

    def __repr__(self):
        if (self._string == ''):
            return 'None'
        return str(self._string)
    
class AdvRandomList(RemapList):
    def __init__(self, groups = None):
        super().__init__(groups)
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()


s = GroupList()

print(s)

s += 12345

print(s)