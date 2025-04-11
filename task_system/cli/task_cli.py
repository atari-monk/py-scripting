from task_system.cli.TaskApiClient import TaskApiClient
from task_system.cli.TaskCLI import TaskCLI

def main():
    client = TaskApiClient()
    cli = TaskCLI(client)
    
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()