# NeditGD

 Lightweight Geometry Dash level scripting tool

 This fork is a WIP, I'm currently overhauling it to make it more user friendly.

## Installation

 This fork can only be installed manually; add to project path.

## TODO
- Particles
- Type checks
- Other

## WIP

### Object Classes

In this version, a variety of Object classes are generated using data from [this website](https://flowvix.github.io/gd-info-explorer/props). You can run the various Generator scripts to generate new classes and enums from the data downloaded here if it updates. Under `Dictionaries/ObjectClasses.py`, there are a whole bunch of new classes for objects, that contain properties that those objects have in game, instead of just using property keys and guessing the name.

In Geometry Dash, multiple keys are reused depending on the object, which makes having a static list define all of their names impractical. By using my generated classes, you don't have to cross reference to make sure the properties are correct. If a specific object type is not used, use `Common`, which is the base class for all objects. Below is an example:

 ```python
# Everything you need can be imported like so
from NeditGD import *

# Initialize for websocket editing (what i use)
editor = Editor().load_live_editor()

# Create a pulse trigger and place it at (30, 30)
pulse = PulseTrigger(x = 30, y = 30)

# Set the target channel
pulse.target_id = 10

# Add to the editor
editor.add_object(pulse)

# Save changes
editor.save_changes()

```
Along with this change, printing objects may look a little different now too. Default object strings now contain extra data to identify them better. The format is as follows: 
- `Class | Properties | Object Name (optional) | UUID`

Example:
- `PulseTrigger|(id=1006, x=30, y=30, target_id=10, groups=9999)|unknown|b0d745ee-9ae8-4f0b-8ad5-09e11ee5c3bb`


Objects can now be easily serialized by obtaining their string. If you want you can also use `obj.get_robtop_string()` to get the robtop serialized version:

- `1,1006,2,30,3,30,51,10,57,9999`

For example if you wanted to be able to uniquely identify all added objects, you can reference them by their `token` attribute. A `name` can also be set for better organization.


### Editor

Editor object is defined by the collection of GD objects in the given level. It is used to interact with the level save. Saving and loading your changes is explained in the next section.

```python
# Create empty editor
editor = Editor()

obj = Object(...)

# Add an object
editor.add_object(obj)

# Print existing objects
print(editor.read_objects())
```

## Loading the level editor

### Live with Geode

NeditGD supports live editing via [WSLiveEditor](https://github.com/iAndyHD3/WSLiveEditor) by [iAndyHD3](https://github.com/iAndyHD3). This option requires Geode to function. If you don't want to use mods, see the next section

You will need to:

- [Install Geode](https://geode-sdk.org/install)
- [Install the mod](https://geode-sdk.org/faq#how-do-i-install-mods) named "WSLiveEditor"
- Open the editor of the file you want to edit

Then you can load the Editor object like so:

```python
# Load the editor currently opened
editor = Editor.load_live_editor()

# Make all the necessary changes (add/delete objects)
editor.add_object(
    Common(id=8, x=75, y=-15, groups=[12, 42], scale=5)
)

# Make all the necessary changes (add/delete objects)
editor.save_changes()
```

### From savefile (vanilla)

 For now, Nedit can only read the level at the top of the created levels list ('current level'). If you want to edit a level, push it to the top of your levels list in Geometry Dash first.
 The Editor class handles loading and saving the data automatically. You only need to call the level loader, add your objects, and save the changes:

```python
# Load the most recent level using Editor.load_current_level()
editor = Editor.load_current_level()

# Make all the necessary changes (add/delete objects)
editor.add_object(
    Common(id=8, x=75, y=-15, groups=[12, 42], scale=5)
)

# Make all the necessary changes (add/delete objects)
editor.save_changes()
```

## Special group 9999

 With Nedit you can add tens of thousands of objects to your level at a time. If your development process is iterative, they might need to be removed every time you re-run the script. To avoid doing that manually, Nedit uses group 9999 to mark objects as scripted. Upon a Nedit save, every previously existing object with group 9999 will be deleted and replaced with the new ones. Make sure you don't use this group to prevent your manual changes being deleted.
 If you prefer to disable that behaviour for any reason, you can do so by passing False as the second argument whenever loading the editor and adding new objects:

```python

 ...
editor = Editor.load_current_level(remove_scripted=False)

editor.add_objects(your_object_list, mark_as_scripted=False)
```

## Level Version Control

 Due to the way GD saves are structured, Nedit has to load all of the existing levels in a compressed format before extracting/writing data. Therefore a large amount of levels leads to multiple second load times.
 VersionControl.py is a script that allows you to extract data from a GD file and save it in plaintext format for long-term storage. Useful in case you need to test a change - you don't have to create duplicate levels, so the total weight of your GD save becomes significantly lower.
 Finally, you can use this script to store finished projects or ones you aren't planning to work on for a while longer. That further reduces loadtimes, both of Nedit and GD cloud backup itself.

## Credits

- Code written and hosted by Nemo2510
- Code overhaul by nichie
- Live editing introduced by nichie

### Special Thanks

Huge thanks to people who helped me dig for property ids and debug Nedit:

- [Incidius](https://github.com/Incidius)
- Toastium

Other help:

- [FlowVix](https://github.com/FlowVix) - [gd info explorer](https://flowvix.github.io/gd-info-explorer)
- [iAndyHD3](https://github.com/iAndyHD3) - [WSLiveEditor](https://github.com/iAndyHD3/WSLiveEditor)
