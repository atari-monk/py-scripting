import bpy
import bmesh

def create_parametric_plane(name="ParametricPlane", size_x=2.0, size_y=2.0, location=(0, 0, 0)):
    mesh = bpy.data.meshes.new(name + "Mesh")
    
    bm = bmesh.new()
    
    half_x = size_x / 2
    half_y = size_y / 2
    verts = [
        (-half_x, -half_y, 0),
        (half_x, -half_y, 0),
        (half_x, half_y, 0),
        (-half_x, half_y, 0)
    ]
    
    bm_verts = [bm.verts.new(v) for v in verts]
    
    bm.faces.new(bm_verts)
    
    bm.normal_update()
    
    bm.to_mesh(mesh)
    bm.free()
    
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    
    obj.location = location
    
    return obj