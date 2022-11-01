### General modules ###
from .mirror_button import MirrorButton
from ..strings.ids import ids
from ..strings.labels import labels

### Blender modules ###
import bpy

class MirrorMenu(bpy.types.Panel):
    '''
    Class representing the add-on's panel upon pressing F5 (in default configuration)
    '''
    
    bl_idname = ids["MirrorMenu_bl_idname"]
    bl_label = labels["MirrorMenu_bl_label"]
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        row = box.row()
        row.prop(context.scene, "mirror_x", text=labels["MirrorMenu_x_label"])

        row = box.row()
        row.prop(context.scene, "mirror_y", text=labels["MirrorMenu_y_label"])

        row = box.row()
        row.prop(context.scene, "mirror_z", text=labels["MirrorMenu_z_label"])
        
        row = box.row()
        row.prop(context.scene, "global_mirror", text=labels["MirrorMenu_global_mirror_label"])

        layout.separator()

        row = box.row()
        row.prop(context.scene, "mirroring_suffix", text=labels["MirrorMenu_suffix_label"])

        row = box.row()
        row.operator(MirrorButton.bl_idname, text=MirrorButton.bl_label)
