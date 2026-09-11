"""
Saves object data to use later

May be used later with a mod that stores more data about objects
"""

from NeditGD import *
import json, random

editor = Editor().load_live_editor()

OBJECTS = {}

for x in range(50):
    obj = Object(id = 211)

    obj.color_1 = ColorIDs.BLACK
    obj.color_1_hsv_enabled = True
    obj.color_1_hsv = rgb_to_hsvstring(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    obj.x = x * 30

    OBJECTS[obj.token] = { "string": obj.get_robtop_string(), "data": obj.__str__() }

    editor.add_object(obj)
    
# You can also use the 'dump_metadata' flag to use the built in dump
editor.save_changes()

with open('NeditGD/Examples/serialization.json', 'w') as f:
    json.dump(OBJECTS, f, indent=4)