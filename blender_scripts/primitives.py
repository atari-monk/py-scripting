import bpy

def create_plane(name="Plane", size_x=2.0, size_y=2.0, location=(0, 0, 0)):
    bpy.ops.mesh.primitive_plane_add(size=1.0)
    plane = bpy.context.active_object
    plane.name = name
    plane.location = location
    plane.dimensions = (size_x, size_y, 0)
    return plane

def create_cube(name="Cube", dimensions=(2.0, 2.0, 2.0), location=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1.0)
    cube = bpy.context.active_object
    cube.name = name
    cube.location = location
    cube.dimensions = dimensions
    return cube

def create_cylinder(name="Cylinder", radius=1.0, depth=2.0, location=(0, 0, 0), vertices=32):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=radius,
        depth=depth,
        location=location
    )
    cylinder = bpy.context.active_object
    cylinder.name = name
    return cylinder