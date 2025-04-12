import os
from links_shelf.new_link import add_new_link
from shared_library.json.print import print_json

def main():
    config = {
    'base_directory': r'C:\atari-monk\code\text-data\links',
    'file_name_1': 'links.json',
    'file_name_2': 'links_by_category.json'
    }
    base_directory = config['base_directory']
    file_1_path = os.path.join(base_directory, config['file_name_1'])
    file_2_path = os.path.join(base_directory, config['file_name_2'])

    add_new_link(file_1_path, file_2_path)
    print_json(file_1_path)
    print_json(file_2_path)
    input("Enter to close")

if __name__ == "__main__":
    main()
