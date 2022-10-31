### General modules ###
from ..strings.ids import ids
from ..strings.descriptions import descriptions
from ..strings.labels import labels
from .popups import SimplePopup
from ..strings.errors import errors

### Blender modules ###
import bpy
from bpy.types import Operator

class MirrorButton(Operator):
    bl_idname =  ids["MirrorButton_bl_idname"]
    bl_description = descriptions["MirrorButton_bl_description"]
    bl_label = labels["MirrorButton_bl_label"]

    @classmethod
    def poll(cls, context):
        return True
    
    def mirror(self):
        mirror_x = -1.0 if bpy.context.scene.mirror_x == True else 1.0
        mirror_y = -1.0 if bpy.context.scene.mirror_y == True else 1.0
        mirror_z = -1.0 if bpy.context.scene.mirror_z == True else 1.0

        if(len(bpy.context.selected_objects) == 0):
            SimplePopup.showPopup(self, errors["Message_no_objects_selected"])
            return
        
        for obj in bpy.context.selected_objects:
            flipped = obj.copy()
            flipped.name = obj.name + " " + bpy.context.scene.mirroring_suffix
            bpy.ops.object.add_named(name=flipped.name)
            bpy.context.active_object.scale = (mirror_x, mirror_y, mirror_z)
            bpy.context.active_object.name = flipped.name # Without the .001 suffix

    def execute(self, context):
        self.mirror()
        return {"FINISHED"}
        
