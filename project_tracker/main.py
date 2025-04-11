import sys
from project_tracker.args import get_file_path, get_file_paths
from project_tracker.end_task import update_end_time_for_active_tasks
from project_tracker.new_task import add_new_task
from project_tracker.report import generate_markdown_report
from project_tracker.stats import calculate_days_stats
from shared_library.json.print import print_json

config = {
    'base_directory': r'C:\atari-monk\code\text-data\project-tracker',
    'filename': 'tasks.json',
    'filename_1': 'tasks.json',
    'filename_2': 'stats.json'
}

def end_task():
    file_path = get_file_path(config, sys.argv)
    update_end_time_for_active_tasks(file_path)
    print_json(file_path)

def new_task():
    file_path = get_file_path(config, sys.argv)
    add_new_task(file_path)
    print_json(file_path)

def generate_report():
    if len(sys.argv) < 2:
        print("Please provide a report name as argument")
        return
    
    file_1_path, file_2_path = get_file_paths(config, sys.argv)
    report_path = generate_markdown_report(file_1_path, file_2_path, sys.argv[1])
    
    if report_path:
        print(f"Markdown report saved to: {report_path}")
    else:
        print("Error generating the report.")

def update_stats():
    file_1_path, file_2_path = get_file_paths(config, sys.argv)
    calculate_days_stats(file_1_path, file_2_path)
    print_json(file_2_path)

def show_menu():
    print("\nProject Tracker Menu:")
    print("1. Add new task")
    print("2. End active tasks")
    print("3. Update statistics")
    print("4. Generate report")
    print("5. Exit")
    
    try:
        choice = int(input("Enter your choice (1-5): "))
        return choice
    except ValueError:
        print("Please enter a number between 1 and 5")
        return show_menu()

def main():
    while True:
        choice = show_menu()
        
        if choice == 1:
            new_task()
        elif choice == 2:
            end_task()
        elif choice == 3:
            update_stats()
        elif choice == 4:
            report_name = input("Enter report name: ")
            sys.argv.append(report_name)  # Add report name to sys.argv
            generate_report()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        if choice in [1, 2, 3, 4]:
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()