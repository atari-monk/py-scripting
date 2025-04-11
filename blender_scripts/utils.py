import bpy

def apply_all_transforms(obj_names=None):
    """
    Applies location, rotation, and scale transforms to specified objects or all selected objects.
    
    Args:
        obj_names (list, optional): List of object names to apply transforms to. 
                                  If None, applies to all selected objects.
    """
    # If no specific object names are provided, use selected objects
    if obj_names is None:
        objects = bpy.context.selected_objects
    else:
        objects = [bpy.data.objects.get(name) for name in obj_names if bpy.data.objects.get(name)]
    
    if not objects:
        print("No valid objects found to apply transforms")
        return
    
    # Store current selection
    original_selection = bpy.context.selected_objects
    original_active = bpy.context.active_object
    
    # Apply transforms to each object
    for obj in objects:
        # Select only this object
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        
        # Apply transforms
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    
    # Restore original selection
    bpy.ops.object.select_all(action='DESELECT')
    for obj in original_selection:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = original_active

# Example usage:
# apply_all_transforms(["Cabin Size", "Foundation Pillar", "Foundation Pillar Above", "Foundation Pillar Below"])
# Or for selected objects:
# apply_all_transforms()