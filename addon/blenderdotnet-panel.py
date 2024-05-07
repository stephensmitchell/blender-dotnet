bl_info = {
    "name": "blenderdotnet_panel Panel",
    "blender": (4, 1, 1),
    "category": "Object",
}
import bpy
class blenderdotnet_panelPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "blenderdotnet-panel Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    def draw(self, context):
        self.layout.operator("object.blenderdotnet_panel", text="Say Hello")
class blenderdotnet_panelOperator(bpy.types.Operator):
    """My Object Operator"""
    bl_idname = "object.blenderdotnet_panel"
    bl_label = "Print blenderdotnet_panel"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        print("Hello, World!")
        return {'FINISHED'}
def register():
    bpy.utils.register_class(blenderdotnet_panelOperator)
    bpy.utils.register_class(blenderdotnet_panelPanel)
def unregister():
    bpy.utils.unregister_class(blenderdotnet_panelOperator)
    bpy.utils.unregister_class(blenderdotnet_panelPanel)
if __name__ == "__main__":
    register()
