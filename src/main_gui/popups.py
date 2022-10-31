### General modules ###

### Blender modules ###
import bpy
    
class SimplePopup():
    '''
    Create a simple popup to notify the user
    '''
    def showPopup(self, message = "Message", title = "Info", icon = 'INFO'):
        def draw(self, context):
            self.layout.label(text = message)

        bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)
