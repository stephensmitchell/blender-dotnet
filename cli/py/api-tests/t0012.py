import bpy
import os
# Clear existing scene data
bpy.ops.wm.read_factory_settings(use_empty=True)
# Add a new cube to the scene
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), size=82)
# Get the directory of the script file
script_dir = os.path.dirname(os.path.realpath(__file__))
# Save the blend file in the same directory as the script
blend_file_path = os.path.join(script_dir, "output.blend")
bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
