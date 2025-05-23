from NeditGD import Editor, Object, HSV

# This example is the same as 'example.py' but it utilizes the geode mod "WSLiveEditor" by iAndyHD3
# The source code for the mod can be found here: https://github.com/iAndyHD3/WSLiveEditor 
# Everything remains the same, apart from the constructor for Editor,
# which includes a "live_edit" flag, indicating that you are using WSLiveEditor

emitter_id = -1

if __name__ == '__main__':
    editor = Editor.load_current_level(live_edit=True)

    obj = Object(id='block', x=75, y=-15, groups=[12, 42], scale=5)
    obj.hsv_enabled = 1
    obj.hsv = HSV(20, 1.3, 0.7, True)
    editor.add_object(obj)

    obj2 = obj.copy(
        obj,
        x=165
    )
    obj2.id = 'spike'
    editor.add_object(obj2)

    editor.add_object(Object(
        id=1268, #Spawn trigger
        x=15,
        y=15,
        spawn_remap=[(1, 2), (3, 4)]
    ))
    
    editor.save_changes()