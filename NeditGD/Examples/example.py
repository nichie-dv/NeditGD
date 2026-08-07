"""
Makes a nice pattern with toggle triggers
"""

from NeditGD import *
editor = Editor().load_live_editor()

SCALE = 20

for y in range(SCALE):
    for x in range(SCALE):
        index = x + (y * SCALE)
        o = ToggleTrigger(x = (x * 30) + 15, y = (y * 30) + 15)
        o.target_group = index
        if index % 3 == 0: o.activate_group = True
        editor.add_object(o)
        if (index < 10): Log.debug(o)
        
editor.save_changes()