import bpy
import os
# Clear existing scene data
bpy.ops.wm.read_factory_settings(use_empty=True)
# Add a new cube to the scene
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 10))
# Get the reference to the newly added cube object
cube = bpy.context.active_object
# Change the scale dimensions of the cube
cube.dimensions = (20, 10, 3)   # Change the scale to (x=2, y=3, z=1) dimensions
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
# Get the directory of the script file
script_dir = os.path.dirname(os.path.realpath(__file__))
# Save the blend file in the same directory as the script
blend_file_path = os.path.join(script_dir, "output4.blend")
bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
