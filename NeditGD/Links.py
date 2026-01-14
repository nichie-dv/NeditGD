from NeditGD import Object, Editor
from NeditGD.Dictionaries import PropertyID

linked_props = [
    373, 108
]

def get_next_free_group(editor: Editor):
    objects = editor.objects
    print(objects)