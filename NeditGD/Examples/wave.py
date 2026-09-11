"""
Makes a dashed sine wave
"""

from NeditGD import *
import numpy as np

editor = Editor().load_live_editor()

WAVELENGTH = 15
HEIGHT = 60

x2 = 0
y2 = 0

for x in range(360):
    obj = Object(id = 1767)

    x1 = x * WAVELENGTH
    y1 = np.sin(np.radians(x * WAVELENGTH)) * HEIGHT

    dx = x2 - x1
    dy = y2 - y1

    obj.x = x1
    obj.y = y1

    obj.rotation = -np.degrees(np.arctan2(dy, dx))

    editor.add_object(obj)

    x2 = x1
    y2 = y1

editor.save_changes()