"""
Using the rgb_to_hsv function, you may use one color channel for multiple colors
"""

from NeditGD import *
import json

editor = Editor().load_live_editor()

start = (255, 0, 0)      # Red
end   = (0, 0, 255)      # Blue

count = 50

for x in range(count):
    t = x / (count - 1)

    r = start[0] + (end[0] - start[0]) * t
    g = start[1] + (end[1] - start[1]) * t
    b = start[2] + (end[2] - start[2]) * t

    obj = Object(id=211)

    obj.color_1 = ColorIDs.WHITE
    obj.color_1_hsv_enabled = True
    obj.color_1_hsv = rgb_to_hsvstring(r, g, b)

    obj.x = x * 30
    
    editor.add_object(obj)

editor.save_changes()