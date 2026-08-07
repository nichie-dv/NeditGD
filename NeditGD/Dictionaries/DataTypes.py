import json, sys
from NeditGD.Config import Log

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
        Log.error(f'[FATAL] {type(object).__name__} @ {hex(id(object))}: {fault_reason}')
        sys.exit()

    if not fault and not fatal: return True
    
    if Log.LOG_WARNINGS: Log.warn(f'[WARN]: {type(object).__name__} @ {hex(id(object))}: {fault_reason}\nexpected:\n' + json.dumps(expectation, indent=4) + '\ngot:\n' + json.dumps(got, indent=4))

    return False

#TODO: finish this
def check_format(obj, val, expectation, got) -> tuple[bool, bool]:
    """
    Checks if format of value for object is valid.

    Returns:
        tuple[bool, bool]: (Did Fault, Did Fatal Fault)
    
    """

    fault = False
    fatal = False

    

    match (obj):
        case HSVString():
            char_arr = val.split('a')
            seperators = val.count('a')

            if len(char_arr) != seperators + 1:
                fault = True

                expectation['string'] = ['0a0a0', '0a0a0a0a0']
                got['string'] = val
                

            if len(char_arr) not in (3, 5):
                fault = True

                expectation['length'] = [3, 5]
                got['length'] = len(char_arr)
            
        
        case GroupList():
            if isinstance(val, str):
                char_arr = val.split(".")

                for s in char_arr:
                    try:
                        i = int(s)
                    except ValueError:
                        fault = True
                        expectation["data"] = "int"
                        got["data"] = s
                        break

                    if not (0 <= i <= 9999):
                        fault = True
                        expectation["limit"] = "0-9999"
                        got.setdefault("limit", []).append(i)

            elif isinstance(val, int):
                if not (0 <= val <= 9999):
                    fault = True
                    expectation["limit"] = "0-9999"
                    got["limit"] = val

            else:
                fault = True
                expectation["type"] = ["str", "int"]
                got["type"] = type(val).__name__

                
        case RemapList() | AdvRandomList():
            if isinstance(val, list):
                for tup in val:
                    #invalid length of inner
                    if len(tup) != 2:
                        fault = True

                        expectation["inner_length"] = 2
                        got.setdefault("inner_length", []).append(len(tup))
                        continue
                    
                    #invalid characters of inner
                    if not all(isinstance(x, int) for x in tup):
                        fault = True
                        expectation["data"] = "int"
                        got.setdefault("data", []).append(tup)

                    #invalid groups of inner
            
            


            elif isinstance(val, int):
                if val > 9999 or val < 0:
                    fault = True

                    expectation['limit'] = '0-9999'
                    got['limit'] = val

            else:
                fault = True
                expectation["type"] = ["list", "tuple", "int"]
                got["type"] = type(val).__name__
    
    return (fault, fatal)




    

class NInt(int):
    def __new__(cls, value=0):
        return super().__new__(cls, value)

    def __str__(self):
        return str(int(self))

    def __repr__(self):
        return str(int(self))


class NFloat(float):
    def __new__(cls, value=0.0):
        return super().__new__(cls, value)

    def __str__(self):
        return str(float(self))

    def __repr__(self):
        return str(float(self))

class NBool:
    def __init__(self, truth: bool = False):
        self.__truth = truth

    def __eq__(self, other):
        if isinstance(other, NBool):
            return self.__truth == other.__truth
        return self.__truth == other

    def __bool__(self):
        return self.__truth

    def __str__(self):
        return "1" if self.__truth else "0"

    def __repr__(self):
         return "1" if self.__truth else "0"
    
class NString(str):
    def __new__(cls, value=""):
        return super().__new__(cls, value)

    def __str__(self):
        return self.__string

    def __repr__(self):
        return self.__string

    


class HSVString:
    def __init__(self, h = 0, s = 0, v = 0, s_checked = False, v_checked = False):
        self.__h = h
        self.__s = s
        self.__v = v

        self.__s_chk = s_checked
        self.__v_chk = v_checked

        self.__string = f'{h}a{s}a{v}a{int(s_checked)}a{int(v_checked)}'

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, val):
        self.__h = max(min(val, 180), -180)
        self.__update_string()

    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, val):
        self.__s = max(min(val, 180), -180)
        self.__update_string()

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, val):
        self.__v = max(min(val, 180), -180)
        self.__update_string()
    

    def set(self, val: str):
        if not check_data_validity(self, val):
            return self

        parts = val.split("a")

        self.__h = int(parts[0])
        self.__s = int(parts[1])
        self.__v = int(parts[2])

        if len(parts) == 5:
            self.__s_chk = bool(int(parts[3]))
            self.__v_chk = bool(int(parts[4]))

        self.__update_string()
        return self

    def __update_string(self):
        self.__string = (
            f'{self.__h}a{self.__s}a{self.__v}'
            f'a{int(self.__s_chk)}a{int(self.__v_chk)}'
        )

    def __str__(self):
        if (self.__string == ''):
            return 'None'
        return self.__string

    def __repr__(self):
        if (self.__string == ''):
            return 'None'
        return str(self.__string)

    def is_default(self):
        return (
            self.__h == 0 and
            self.__s == 0 and
            self.__v == 0 and
            not self.__s_chk and
            not self.__v_chk
        )

    def __eq__(self, other):
            if isinstance(other, HSVString):
                return self.__string == other.__string
            return False


class GroupList:
    def __init__(self, groups=None):

        if groups is None:
            self.__groups = []

        elif isinstance(groups, str):
            self.__groups = [
                int(x) for x in groups.split(".")
                if x
            ]

        else:
            self.__groups = groups

        self.__string = ''
        self.__update_string()


    def __update_string(self):
        self.__string = ".".join(
            str(x) for x in self.__groups
        )


    def set(self, val: str):
        if not check_data_validity(self, val):
            return self

        self.__groups = [
            int(x) for x in val.split(".")
            if x
        ]

        self.__update_string()

        return self


    @property
    def groups(self):
        return self.__groups


    def __contains__(self, val):
        return val in self.__groups


    def __iter__(self):
        return iter(self.__groups)


    def append(self, val):
        if val not in self.__groups:
            self.__groups.append(val)
            self.__update_string()


    def __add__(self, val: int):
        self.append(val)
        return self


    def __sub__(self, val: int):
        if val in self.__groups:
            self.__groups.remove(val)

        self.__update_string()
        return self


    def __str__(self):
        return self.__string


    def __repr__(self):
        return self.__string


    def __eq__(self, other):
        if isinstance(other, GroupList):
            return self.__groups == other.__groups

        return False



class ParticleString:
    def __init__(self, i: int = 0):
        #TODO: impl
        pass



class RemapList:
    def __init__(self, groups = None):
        self.__groups = groups or []

        self.__string = ''

    def __update_string(self):
        tmp = ''
        for index, val in enumerate(self.__groups):
            tmp += (str(val[0]) + '.' + str(val[1]))
            if (index < len(self.__groups) - 1):
                tmp += '.'

        self.__string = tmp

    @property
    def groups(self):
        return self.__groups

    def __add__(self, val: tuple | list):
        if not check_data_validity(self, val):
            return self

        if (type(val) == tuple):
            if (val not in self.__groups):
                self.__groups.append(val)

        if (type(val) == list):
            for entry in val:
                if (entry not in self.__groups) and type(entry) == tuple:
                    self.__groups.append(entry)

        self.__update_string()
        return self

    def __sub__(self, val: tuple | list):
        if (type(val) == tuple):
            if (val in self.__groups):
                self.__groups.remove(val)

        if (type(val) == list):
            for entry in val:
                if (entry in self.__groups) and type(entry) == tuple:
                    self.__groups.remove(entry)

        self.__update_string()
        return self
    
    def __str__(self):
        if (self.__string == ''):
            return 'None'
        return self.__string

    def __repr__(self):
        if (self.__string == ''):
            return 'None'
        return str(self.__string)
    
class AdvRandomList(RemapList):
    def __init__(self, groups = None):
        super().__init__(groups)
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
class SequenceList(RemapList):
    def __init__(self, sequence = None):
        super().__init__(sequence)
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()

class EventList(GroupList):
    def __init__(self, events = None):
        super().__init__(events)
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    

