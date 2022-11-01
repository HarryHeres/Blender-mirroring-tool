### General libraries ###
from .main_gui.mirror_button import MirrorButton
from .main_gui.mirror_menu import MirrorMenu
from .strings.keymaps import keymaps
from .strings.descriptions import descriptions

### Blender libraries ###
import bpy
from bpy.utils import register_class, unregister_class

_props = []
'''
Add-on properties
'''

_classes = [MirrorButton, MirrorMenu]
'''
Add-on classes
'''

_keymaps_list = []


bl_info = {
 "name": "Better Mirroring Add-on",
 "description": "Addon used for better mirroring functionality than Blender offers by default",
 "author": "Jan Hereš (www.janheres.eu)",
 "blender": (2, 93, 0),
 "version": (1, 0, 0),
 "warning": "Only officially supported for versions 2.91.X - 2.93.X of Blender!",
 "category": "Object",
}
'''
Add-on info in Edit -> Preferences -> Add-ons
'''

def register():
    register_classes()
    register_props()
    register_keymaps()

def register_classes():
    global _classes

    for cls in _classes:
        register_class(cls)


def register_props():
    bpy.types.Scene.mirror_x = bpy.props.BoolProperty(
        name = "Mirroring X-Axis",
        default=False
    )

    bpy.types.Scene.mirror_y = bpy.props.BoolProperty(
        name = "Mirroring Y-Axis",
        default=False
    )

    bpy.types.Scene.mirror_z = bpy.props.BoolProperty(
        name = "Mirroring Z-Axis",
        default=False
    )
    
    bpy.types.Scene.mirroring_suffix = bpy.props.StringProperty(
            name = "Mirroring suffix",
            default = "",
            description = descriptions["MirrorMenu_suffix_description"],
    )

    bpy.types.Scene.global_mirror = bpy.props.BoolProperty(
            name = "Global Mirror",
            default = True
    )


    _props.append(bpy.types.Scene.mirror_x)
    _props.append(bpy.types.Scene.mirror_y)
    _props.append(bpy.types.Scene.mirror_z)
    _props.append(bpy.types.Scene.global_mirror)

def register_keymaps():
    global _keymaps_list

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    for keymap_group_name in keymaps:
        keylist = keymaps[keymap_group_name]

        for list_item in keylist:
            menu_name = list_item.get("menu_name")
            space_type = list_item.get("space_type", "EMPTY")
            region_type = list_item.get("region_type", "WINDOW")

            if list_item:
                km = kc.keymaps.new(menu_name, space_type=space_type, region_type=region_type)

                if km:
                    action = list_item.get("action")
                    idname = list_item.get("idname")
                    type = list_item.get("type")
                    value = list_item.get("value")

                    shift = list_item.get("shift", False)
                    ctrl = list_item.get("ctrl", False)
                    alt = list_item.get("alt", False)
                    oskey = list_item.get("oskey", False)

                    kmi = km.keymap_items.new(action, type, value, shift=shift, ctrl=ctrl, alt=alt, oskey=oskey)

                    if kmi:
                        kmi.properties.name = idname
                _keymaps_list.append(km)

def unregister():
    for cls in _classes:
        unregister_class(cls)
    
    for prop in _props:
        del prop

    unregister_keymaps()

def unregister_keymaps():
    global _keymaps_list

    wm = bpy.context.window_manager

    for km in _keymaps_list:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
    _keymaps_list.clear()
            


if __name__ == "__main__":
    register()
