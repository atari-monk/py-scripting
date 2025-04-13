import logging
import argparse
from log_project.project import Project
from log_project.project_crud import ProjectCRUD

logger = logging.getLogger(__name__)

def add_project():
    parser = argparse.ArgumentParser(description="Add a new project.")
    parser.add_argument("name", help="Name of the project")
    parser.add_argument("description", help="Description of the project")
    parser.add_argument("--repo_link", help="Repository link", default=None)
    parser.add_argument("--status", 
                       choices=Project.STATUS_CHOICES,
                       help="Project status", default=None)
    parser.add_argument("--start_date", help="Start date (YYYY-MM-DD)", default=None)
    parser.add_argument("--end_date", help="End date (YYYY-MM-DD)", default=None)
    parser.add_argument("--priority", 
                       choices=Project.PRIORITY_CHOICES,
                       help="Project priority", default=None)
    parser.add_argument("--technologies", help="Comma-separated list of technologies", default="")
    parser.add_argument("--milestones", help="Comma-separated list of milestones", default="")
    parser.add_argument("--current_tasks", help="Comma-separated list of current tasks", default="")

    args = parser.parse_args()

    try:
        project_crud = ProjectCRUD()
        
        project = Project(
            name=args.name,
            description=args.description,
            repo_link=args.repo_link,
            status=args.status,
            start_date=args.start_date,
            end_date=args.end_date,
            priority=args.priority,
            technologies=args.technologies,
            milestones=args.milestones,
            current_tasks=args.current_tasks
        )

        result = project_crud.add_item(project.to_dict())
        
        if result:
            logger.info(f"Project '{args.name}' created successfully.")
        else:
            logger.warning("Failed to create project.")
    except ValueError as e:
        logger.error(f"Validation error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during project creation: {e}")

if __name__ == "__main__":
    add_project()