import os

def get_first_existing_path(paths):
    for path in paths:
        if os.path.exists(path):
            return path
    return None

# Example usage:
# paths_to_check = ['/path/one', '/path/two', '/path/three']
# existing_path = get_first_existing_path(paths_to_check)
# print(existing_path)