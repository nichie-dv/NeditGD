"""
A niche use case involves being able to store data in levels with objects,
though a better way is to use the guideline string.

kA14 is the guideline string key.

This only works in save file editing, as WSLiveEditor only supports adding/removing objects.

JSON is preferred, but a raw string is also accepted. XML is not implemented yet.
"""

from NeditGD import *

editor = Editor.load_current_level()

data = editor.get_save_string()
Log.info(data)

data["my-data"] = {
    "enabled": True,
    "name": "Example",
    "value": 123,
}

editor.set_save_string(data)
editor.save_changes()