from NeditGD import *

editor = Editor.load_live_editor()




for y in range(100):
    for x in range(100):
        index = y * 100 + x

        c = PickupTrigger()
        c.item_id = index

        c.x = x * 15
        c.y = y * 15

        c.count = -2147483648

        s = CounterLabel()

        s.item_id = index
        s.x = x * 15 + 2000
        s.y = y * 15

        editor.add_object(c)
        editor.add_object(s)

editor.save_changes()