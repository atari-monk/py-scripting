import logging
import argparse
from log_project.project_crud import ProjectCRUD2

logger = logging.getLogger(__name__)

def add_project():
    parser = argparse.ArgumentParser(description="Add a new project.")
    parser.add_argument('name', help='Name of the project')
    parser.add_argument('description', help='Description of the project')
    parser.add_argument('--repo_link', help='Repository link', default=None)
    parser.add_argument('--status', help='Project status', default=None)
    parser.add_argument('--start_date', help='Project start date', default=None)
    parser.add_argument('--end_date', help='Project end date', default=None)
    
    args = parser.parse_args()
    
    project_json_reposotory = ProjectCRUD2()
    #project_jsonl_reposotory = ProjectCRUD3()

    project_dict = {
        'id': 0,
        'name': args.name,
        'description': args.description,
        'repo_link': args.repo_link,
        'status': args.status,
        'start_date': args.start_date,
        'end_date': args.end_date
    }

    try:
        result = project_json_reposotory.add_item(project_dict)
        result_jsonl = True #project_jsonl_reposotory.add_item(project_dict)
        if result and result_jsonl:
            logger.info(f"Project '{result['name']}' created successfully with ID '{result['id']}' in both repositories (JSON and JSONL).")
        else:
            if not result:
                logger.warning("Failed to create project in JSON repository.")
            if not result_jsonl:
                logger.warning("Failed to create project in JSONL repository.")
    except Exception as e:
        logger.error(f"Unexpected error during project creation: {e}")

if __name__ == "__main__":
    add_project()