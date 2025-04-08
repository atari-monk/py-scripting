import sys
sys.path.append(r"C:\atari-monk\code\py-scripting\blender")
import plane

plane.create_parametric_plane(
    name="ModularPlane",
    size_x=5.0,
    size_y=5.0,
    location=(0, 0, 0)
)