import sys
sys.path.append(r'C:\atari-monk\code\py-scripting\blender_scripts')
from utils import apply_all_transforms
from primitives import create_cube, create_plane


cabin_size = create_plane("Cabin Size", size_x=6, size_y=5)
foundation_pillar = create_cube("Foundation Pillar", dimensions=(.3, .3, 1.9), location=(-2.85, -2.35, -(1.9/2 - 0.7)))
above_ground_pillar = create_cube("Foundation Pillar Above", dimensions=(.3, .3, .7), location=(-2.85 - .3, -2.35, .7/2))
below_ground_pillar = create_cube("Foundation Pillar Below", dimensions=(.3, .3, 1.9-.7), location=(-2.85-.3, -2.35, -1.2/2))

apply_all_transforms(["Cabin Size", "Foundation Pillar", "Foundation Pillar Above", "Foundation Pillar Below"])