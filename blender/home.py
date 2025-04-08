import sys
sys.path.append(r"C:\atari-monk\code\py-scripting\blender")
import primitives

cabin_size = primitives.create_plane("Cabin Size", size_x=6, size_y=5)
foundation_pillar = primitives.create_cube("Foundation Pillar", dimensions=(.3, .3, 1.7), location=(0, 0, 0.4))
