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
        
        if(len(bpy.context.selected_objects) == 0):
            SimplePopup.showPopup(self, errors["Message_no_objects_selected"], "INFO", "INFO")
            return
        
        selected = bpy.context.selected_objects
        
        for obj in selected:
            if(bpy.context.scene.global_mirror == True):
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True) # The object origin point is moved to the global origin, the rotation is cleared and scale values are set to 1
                     
            mirror_x = -1.0 * obj.scale[0] if bpy.context.scene.mirror_x == True else obj.scale[0]
            mirror_y = -1.0 * obj.scale[1] if bpy.context.scene.mirror_y == True else obj.scale[1]
            mirror_z = -1.0 * obj.scale[2] if bpy.context.scene.mirror_z == True else obj.scale[2]

            mirrored = obj.copy()    
            mirrored.name = obj.name + " " + bpy.context.scene.mirroring_suffix

            bpy.ops.object.add_named(name=mirrored.name)
            mirrored.name = mirrored.name
            bpy.context.active_object.scale = (mirror_x, mirror_y, mirror_z)
            if(bpy.context.scene.mirroring_suffix != ""):
                bpy.context.active_object.name = mirrored.name # Remove the Blender numbering (.00X)

        # Deselect all newly created and select back the original ones
        bpy.ops.object.select_all(action="DESELECT") 
        for obj in selected:
            obj.select_set(True)
            

    def execute(self, context):
        self.mirror()
        return {"FINISHED"}
        
