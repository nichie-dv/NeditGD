from __future__ import annotations
from websocket import create_connection
import json


from NeditGD.Dictionaries.ObjectClasses import *

from NeditGD.saveload import *

from NeditGD.Config import Log, PrefixType


CLASS_TO_ID = {
    "Common": 1,
    "DashOrb": 1704,
    "CustomParticles": 2065,
    "TextObject": 914,
    "Collectible": 1329,
    "RotatingObject": 1705,
    "AnimatedObject": 1050,
    "KeyframeObject": 3032,
    "Trigger": 1049,
    "ColorTrigger": 899,
    "BackgroundColorTrigger": 29,
    "BackgroundSpeedTrigger": 3606,
    "MiddleGroundSpeedTrigger": 3612,
    "EditMiddleGroundTrigger": 2999,
    "MoveTrigger": 901,
    "PulseTrigger": 1006,
    "AlphaTrigger": 1007,
    "ToggleTrigger": 1049,
    "ShakeTrigger": 1520,
    "AnimateTrigger": 1585,
    "SpawnTrigger": 1268,
    "RotateTrigger": 1346,
    "ScaleTrigger": 2067,
    "FollowTrigger": 1347,
    "StopTrigger": 1616,
    "KeyframeAnimTrigger": 3033,
    "FollowPlayerYTrigger": 1814,
    "AdvancedFollowTrigger": 3016,
    "EditAdvancedFollowTrigger": 3660,
    "RetargetAdvancedFollowTrigger": 3661,
    "AreaTrigger": 3006,
    "EditAreaTrigger": 3011,
    "AreaMoveTrigger": 3006,
    "EditAreaMoveTrigger": 3011,
    "AreaRotateTrigger": 3007,
    "EditAreaRotateTrigger": 3012,
    "AreaScaleTrigger": 3008,
    "EditAreaScaleTrigger": 3013,
    "AreaFadeTrigger": 3009,
    "EditAreaFadeTrigger": 3014,
    "AreaTintTrigger": 3010,
    "EditAreaTintTrigger": 3015,
    "StopAreaTrigger": 3024,
    "BackgroundTrigger": 3029,
    "GroundTrigger": 3030,
    "MiddleGroundTrigger": 3031,
    "TouchTrigger": 1595,
    "CountTrigger": 1611,
    "InstantCountTrigger": 1811,
    "GradientTrigger": 2903,
    "StaticCameraTrigger": 1914,
    "CameraZoomTrigger": 1913,
    "CameraRotateTrigger": 2015,
    "CameraEdgeTrigger": 2062,
    "CameraModeTrigger": 2925,
    "CameraGuide": 2016,
    "CameraOffsetTrigger": 1916,
    "SongTrigger": 1934,
    "SFXTrigger": 3602,
    "PickupTrigger": 1817,
    "TimeTrigger": 3614,
    "TimeEventTrigger": 3615,
    "TimeControlTrigger": 3617,
    "ItemEditTrigger": 3619,
    "ItemCompareTrigger": 3620,
    "ItemPersistenceTrigger": 3641,
    "RandomTrigger": 1912,
    "AdvancedRandomTrigger": 2068,
    "SequenceTrigger": 3607,
    "SpawnParticleTrigger": 3608,
    "ResetTrigger": 3618,
    "ArrowTrigger": 2900,
    "EventTrigger": 3604,
    "TimewarpTrigger": 1935,
    "CounterLabel": 1615,
    "UITrigger": 3613,
    "CollisionTrigger": 1815,
    "InstantCollisionTrigger": 3609,
    "CollisionStateBlock": 3640,
    "CollisionBlock": 1816,
    "ToggleBlock": 3643,
    "OptionsTrigger": 2899,
    "OnDeathTrigger": 1812,
    "GravityTrigger": 2066,
    "PlayerControlTrigger": 1932,
    "TeleportTrigger": 3022,
    "BlueTeleportal": 747,
    "TeleportOrb": 3027,
    "ShaderTrigger": 2904,
    "ShockwaveShaderTrigger": 2905,
    "ShockLineShaderTrigger": 2907,
    "GlitchShaderTrigger": 2909,
    "ChromaticShaderTrigger": 2910,
    "ChromaGlitchShaderTrigger": 2911,
    "PixelateShaderTrigger": 2912,
    "LensCircleShaderTrigger": 2913,
    "RadialBlurShaderTrigger": 2914,
    "MotionBlurShaderTrigger": 2915,
    "BulgeShaderTrigger": 2916,
    "PinchShaderTrigger": 2917,
    "GrayscaleShaderTrigger": 2919,
    "SepiaShaderTrigger": 2920,
    "InvertColorShaderTrigger": 2921,
    "HueShaderTrigger": 2922,
    "EditColorTrigger": 2923,
    "EnterEffectTrigger": 3017,
    "EditSongTrigger": 3605,
    "EditSFXTrigger": 3603,
    "ForceBlock": 2069,
    "EndTrigger": 3600,
    "SecretCoin": 142,
    "OldEndTrigger": 1931,
    "Template": 2895,
    "CheckpointTrigger": 2063,
    "BPMGuide": 3642,
}

ID_TO_CLASSES = {}

BASE_IDS = []

for class_name, object_id in CLASS_TO_ID.items():
    ID_TO_CLASSES.setdefault(object_id, []).append(class_name)

for class_name, object_id in CLASS_TO_ID.items():
    BASE_IDS.append(object_id)


WATERMARK_TEXT = [
    TextObject(id=914, x=-165, y=-15, scale=0.75, text="Made with Nedit"),
    TextObject(id=914, x=-165, y=-30, scale=0.5, text="by Nemo2510 and nichie"),
    TextObject(id=914, x=-175, y=-41, scale=0.35, text="github.com/Boris-Filin/NeditGD"),   
    TextObject(id=914, x=-147, y=-56, scale=0.2, text="(You can remove this watermark, but we'd appreciate it if you didn't)"),
]

PAD = ' ' * 8

# The class that stores all loaded objects and handles
# interactions with the SaveLoad system for the user
# Behaves as singleton if only one instance exists ('last')
class Editor:
    default_layer = 20
    __last: Editor | None = None


    def __init__(self, live_edit: bool = True):
        self.__root = None
        self.__level_node = None
        self.__level_string = None
        self.__markers = None

        self.head = None
        self.objects: list[Common] = []

        self.raw_level = ""

        self.loaded_obj_count = 0

        self.live_edit = live_edit

        Editor.__last = self

        if live_edit: self.init_socket()


    # ------------------
    # Websocket
    # ------------------

    def init_socket(self):
        try:
            self.socket = create_connection("ws://127.0.0.1:1313")
        except ConnectionRefusedError:
            Log.warn('No editor socket found! Enable WSLiveEdit and open Geometry Dash.', PrefixType.WEBSOCKET)
            raise ConnectionRefusedError()



    def socket_load_data(self):
        packet = { "action": "GET_LEVEL_STRING" }

        self.socket.send(json.dumps(packet))
        response = json.loads(self.socket.recv())


        if response["status"] != "successful":
            Log.warn('Failed reading level', PrefixType.WEBSOCKET)
            raise ConnectionError()
            


        self.raw_level = response["response"]

        self.objects = read_level_objects(self.raw_level)


    def socket_remove_group(self, group: int = 9999):
        Log.debug(f'Removing group {group}', PrefixType.WEBSOCKET)
        self.socket.send(
            json.dumps(
                {
                    "action": "REMOVE_OBJECTS",
                    "group": group
                }
            )
        )



    def socket_save_objects(self):
        objects = self.get_scripted_objects()

        data = ";".join(
            obj.get_robtop_string()
            for obj in objects
        )

        self.socket.send(json.dumps({
            "action": "ADD_OBJECTS",
            "objects": data
        }))

        response = json.loads(self.socket.recv())

        if response["status"] != "successful":
            Log.error(f"Failed adding objects: {response}")
            return False

        return True


    def get_obj_by_token(self, token: str):
        for obj in self.objects:
            if token == obj.token:
                return obj
        return None

    @classmethod
    def load_live_editor(cls, load_existing=True, remove_scripted=True):

        editor = cls(True)
        Log.info("Using current level", PrefixType.WEBSOCKET)


        if load_existing: editor.socket_load_data()
        else: editor.objects = []


        if remove_scripted:
            editor.socket_remove_group(9999)
            editor.remove_scripted_objects()


        return editor
    



    # -==============-
    # SAVEFILE LOADING
    # -==============-

    @classmethod
    def load_current_level(cls, remove_scripted: bool = True) -> Editor:
        editor = Editor(live_edit=False)
        editor.load_level_data()

        if remove_scripted: editor.remove_scripted_objects()

        editor.refresh_markers()
        return editor


    def load_level_data(self, data: str = None) -> None:
        self.__root = read_gamesave_xml()
        self.__level_node = get_working_level_node(self.__root)

        if not self.__level_node.text:
            self.load_default_level()
            return

        level_data = get_working_level(self.__level_node)

        if data: self.__level_string = data
        else: self.__level_string = get_working_level_string(level_data)

        self.head = read_level_head(self.__level_string)

        self.objects = read_level_objects(self.__level_string)

        self.loaded_obj_count = len(self.objects)


    def load_default_level(self) -> None:
        try:
            path = os.path.join( os.path.dirname(os.path.realpath(__file__)), "DefaultLevel")

            with open(path, "r") as f: data = f.read()

        except:
            Log.warn("Default level data missing!", PrefixType.NORMAL)
            raise FileNotFoundError()

        self.head = read_level_head(data)
        self.objects = []

        Log.success("Level initialised successfully!", PrefixType.NORMAL)


    @classmethod
    def load_from_robtop(cls, robtop: str) -> Editor:
        editor = Editor(live_edit=False)
        editor.load_level_data(robtop)
        return editor


    @classmethod
    def get_last(cls):
        if cls.__last is None:
            Log.warn('Editor has not been initialized!', PrefixType.NORMAL)
            raise ReferenceError()

        return cls.__last


    def refresh_markers(self):
        from NeditGD.Nextra.marker_loader import MarkerLoader
        self.__markers = MarkerLoader(self)



    # ----------------
    # OBJECT MANAGEMENT
    # ----------------


    def remove_scripted_objects(self):
        self.objects = [
            obj for obj in self.objects
            if obj.groups is None or 9999 not in obj.groups
        ]

        self.loaded_obj_count = len(self.objects)



    def get_scripted_objects(self):
        return [obj for obj in self.objects if obj.groups is not None and 9999 in obj.groups]



    def add_object(self, obj: Common, mark_as_scripted=True):

        if mark_as_scripted: self.add_group(obj, 9999)

        self.objects.append(obj)



    @staticmethod
    def add_group_to_all(objects: list[Common], group:int):
        for obj in objects: Editor.add_group(obj, group)



    @staticmethod
    def add_group(obj: Common, group:int):
        if obj.groups is None: obj.groups = [group]
        elif group not in obj.groups: obj.groups.append(group)



    def add_objects(self, objects:list[object], mark_as_scripted=True, message=''):

        for obj in objects: self.add_object(obj, mark_as_scripted)
        extra = f"\n{PAD}^ {message}" if message else ""

        Log.success(f"Added {len(objects)} objects to editor.{extra}", PrefixType.NORMAL)



    def read_objects(self):
        return "\n".join(str(obj) for obj in self.objects)



    # ----------------
    # SAVING
    # ----------------


    def save_changes(self, dump_metadata=False):
        self.add_objects(WATERMARK_TEXT, message="Watermark")
        delta = len(self.objects)-self.loaded_obj_count
        Log.info(f"Added {delta} objects total.", PrefixType.NORMAL)

        #Will be used with a mod to reference specific objects by their uuid
        #very rudementary for now
        if (dump_metadata):
            with open('meta.json', 'w') as f:
                data = {}
                for obj in self.objects:
                    data[obj.token] = obj.get_robtop_string() + '|' + obj.name + '|' + (ID_TO_CLASSES[obj.id][0] if obj.id in BASE_IDS else ID_TO_CLASSES[1][0])

                json.dump(data, f, indent=4)

        save_string = self.get_robtop_string()

        if self.live_edit: self.save_changes_live(save_string)
        else: self.save_changes_to_file(save_string)



    def save_changes_to_file(self, save_string:str):

        encrypted = encrypt_level_string(save_string.encode())
        set_level_data(self.__level_node, encrypted)

        xml = ET.tostring(self.__root)

        encryptGamesave(xml)

        Log.success("Changes saved!", PrefixType.NORMAL)



    def save_changes_live(self, save_string:str):
        self.socket_save_objects()
        Log.success("Changes sent successfully", PrefixType.WEBSOCKET)



    def get_robtop_string(self):
        return ";".join([obj.get_robtop_string() for obj in self.objects])



    # ----------------
    # GROUP HELPERS
    # ----------------


    @staticmethod
    def get_max_group(objects:list[object]):
        groups=set()
        for obj in objects:
            if obj.groups: groups.update(obj.groups)


        groups.discard(9999)
        return max(groups) if groups else 0



    @staticmethod
    def get_used_groups(objects:list[object]):
        groups=set()

        for obj in objects:
            if obj.groups: groups.update(obj.groups)


        return list(groups)



    @staticmethod
    def get_intervals(vals:list[int]):

        if not vals: return None


        result=[]
        start=None


        for i in range(min(vals), max(vals)+1):
            if i in vals:
                if start is None: start=i
            elif start is not None:
                result.append((start, i - 1))
                start=None


        return result



    # ----------------
    # MARKERS
    # ----------------


    def get_marker_position(self,name):
        return self.__markers.read_position(name)


    def get_marker_groups(self,name):
        return self.__markers.read_groups(name)


    def get_marker_group1(self,name):
        return self.get_marker_groups(name)[0]


    def get_marker_var(self,name):
        return self.__markers.read_var(name)


    def get_marker_var_int(self,name):
        return self.__markers.read_var_int(name)