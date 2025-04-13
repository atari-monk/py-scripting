import logging
import argparse
from log_project.project_crud import ProjectCRUD

logger = logging.getLogger(__name__)

def delete_project(project_id: int) -> None:
    project_crud = ProjectCRUD()
    
    logger.debug(f"Attempting to delete project with ID: {project_id}")
    
    try:
        existing_project = project_crud.get_by_id(project_id)
        if not existing_project:
            logger.error(f"Project with ID '{project_id}' not found.")
            return

        result = project_crud.delete_by_id(project_id)
        if result:
            logger.info(f"Project '{project_id}' deleted successfully.")
        else:
            logger.warning(f"Failed to delete project '{project_id}'.")
    except ValueError:
        logger.error("Invalid project ID. Please provide a numeric ID.")
    except Exception as e:
        logger.error(f"Unexpected error during project deletion: {e}")

def main():
    parser = argparse.ArgumentParser(description="Delete a project by its ID.")
    parser.add_argument('project_id', type=int, help='The ID of the project to delete')
    args = parser.parse_args()
    
    delete_project(args.project_id)

if __name__ == "__main__":
    main()