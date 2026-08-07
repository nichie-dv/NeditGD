from NeditGD import *
editor = Editor().load_live_editor()

pulse = PulseTrigger(x = 30, y = 30)

if (True): pulse.target_id = 10
else: pulse.target_id = 20

editor.add_object(pulse)

editor.save_changes()