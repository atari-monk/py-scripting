Here are utility functions to manage collections and parenting in Blender:

```python
import bpy

def create_collection(collection_name, parent_collection=None):
    """
    Creates a new collection. If it already exists, returns the existing one.

    Args:
        collection_name (str): Name of the collection to create
        parent_collection (str|bpy.types.Collection): Parent collection name or object.
                                                     If None, adds to scene root.

    Returns:
        bpy.types.Collection: The created or existing collection
    """
    # Create new collection or get existing one
    if collection_name not in bpy.data.collections:
        new_col = bpy.data.collections.new(collection_name)

        # Add to parent or scene root
        if parent_collection is None:
            bpy.context.scene.collection.children.link(new_col)
        else:
            if isinstance(parent_collection, str):
                parent = bpy.data.collections.get(parent_collection)
                if parent:
                    parent.children.link(new_col)
                else:
                    bpy.context.scene.collection.children.link(new_col)
            else:
                parent_collection.children.link(new_col)
    else:
        new_col = bpy.data.collections[collection_name]

    return new_col

def move_to_collection(obj, collection_name, move=True, create_if_missing=True):
    """
    Moves or links an object to a collection.

    Args:
        obj (bpy.types.Object): Object to move
        collection_name (str): Target collection name
        move (bool): If True, removes from other collections. If False, links while keeping existing.
        create_if_missing (bool): If True, creates collection if it doesn't exist

    Returns:
        bool: True if successful, False otherwise
    """
    if not obj:
        return False

    # Get or create collection
    target_col = bpy.data.collections.get(collection_name)
    if not target_col:
        if create_if_missing:
            target_col = create_collection(collection_name)
        else:
            return False

    # Link to new collection
    try:
        target_col.objects.link(obj)
    except RuntimeError:
        pass  # Already in collection

    # Optionally unlink from other collections
    if move:
        for col in obj.users_collection:
            if col != target_col:
                col.objects.unlink(obj)

    return True

def parent_object(child_obj, parent_obj, keep_transform=True):
    """
    Parents one object to another.

    Args:
        child_obj (bpy.types.Object): Object to be parented
        parent_obj (bpy.types.Object): Parent object
        keep_transform (bool): If True, maintains child's world transform

    Returns:
        bool: True if successful, False otherwise
    """
    if not child_obj or not parent_obj:
        return False

    # Store current selection
    original_selection = bpy.context.selected_objects
    original_active = bpy.context.active_object

    # Select objects for parenting
    bpy.ops.object.select_all(action='DESELECT')
    child_obj.select_set(True)
    parent_obj.select_set(True)
    bpy.context.view_layer.objects.active = parent_obj

    # Perform parenting
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=keep_transform)

    # Restore selection
    bpy.ops.object.select_all(action='DESELECT')
    for obj in original_selection:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = original_active

    return True

# Example usage:
# Create collections hierarchy
# main_col = create_collection("Cabin")
# walls_col = create_collection("Walls", main_col)
# foundation_col = create_collection("Foundation", main_col)

# Create objects and organize them
# cabin_size = primitives.create_plane("Cabin Size", size_x=6, size_y=5)
# move_to_collection(cabin_size, "Cabin")

# foundation_pillar = primitives.create_cube("Foundation Pillar", ...)
# move_to_collection(foundation_pillar, "Foundation")
# parent_object(foundation_pillar, cabin_size)
```

Key features of these utilities:

1. `create_collection()`:

   - Creates new collections or returns existing ones
   - Supports nested collections via parent parameter
   - Defaults to scene root if no parent specified

2. `move_to_collection()`:

   - Can either move (exclusive) or link (additive) objects to collections
   - Optionally creates missing collections
   - Handles cases where object is already in target collection

3. `parent_object()`:
   - Safely parents objects while maintaining transforms
   - Preserves original selection state
   - Uses Blender's parenting operator for proper relationship setup

These functions handle edge cases and maintain Blender's selection state, making them safe to use in more complex scripts. They can be used together to create a well-organized scene hierarchy.

Example workflow:

1. Create collections hierarchy
2. Create objects
3. Move objects to appropriate collections
4. Set up parenting relationships
5. Apply transforms as needed
