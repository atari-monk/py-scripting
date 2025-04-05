import os
import shutil
import argparse

def remove_folder_content(folder_path):
    try:
        if not os.path.exists(folder_path):
            print(f"Error: The path '{folder_path}' does not exist.")
            return False
        
        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a directory.")
            return False
        
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        
        print(f"Successfully removed all content from '{folder_path}'.")
        return True
    
    except Exception as e:
        print(f"An error occurred while removing content: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Remove all content from a specified folder.')
    parser.add_argument('--path', type=str, help='Path to the folder whose content will be removed.')
    
    args = parser.parse_args()
    
    if args.path:
        folder_path = args.path
    else:
        folder_path = input("Enter the path of the folder to remove all content: ")
    
    folder_path = os.path.normpath(folder_path)
    
    print(f"WARNING: This will remove ALL content inside '{folder_path}'.")
    confirmation = input("Are you sure you want to proceed? (y/n): ").strip().lower()
    
    if confirmation == 'y':
        remove_folder_content(folder_path)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()