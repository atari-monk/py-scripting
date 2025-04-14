import argparse
import logging
from log_project2.crud.ProjectCRUD import ProjectCRUD
from log_project2.crud.ProjectCRUDJsonl import ProjectCRUDJsonl

logger = logging.getLogger(__name__)

def delete_project_json(project_id: int) -> bool:
    json_repo = ProjectCRUD()
    
    try:
        if not json_repo.get_by_id(project_id):
            logger.error(f"Project {project_id} not found in JSON repository")
            return False
            
        json_success = json_repo.delete_by_id(project_id)
        
        if json_success:
            logger.info(f"Deleted project {project_id} from JSON repository")
            return True
        else:
            logger.error(f"Failed to delete project {project_id} from JSON repository")
            return False
    except Exception as e:
        logger.error(f"Error deleting project from JSON repository: {e}")
        return False

def delete_project_jsonl(project_id: int) -> bool:
    jsonl_repo = ProjectCRUDJsonl()
    
    try:
        if not jsonl_repo.get_by_id(project_id):
            logger.error(f"Project {project_id} not found in JSONL repository")
            return False
            
        jsonl_success = jsonl_repo.delete_by_id(project_id)
        
        if jsonl_success:
            logger.info(f"Deleted project {project_id} from JSONL repository")
            return True
        else:
            logger.error(f"Failed to delete project {project_id} from JSONL repository")
            return False
    except Exception as e:
        logger.error(f"Error deleting project from JSONL repository: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Delete a project by ID")
    parser.add_argument("project_id", type=int, help="Numeric project ID to delete")
    parser.add_argument("--json", action="store_true", help="Delete from JSON repository only")
    parser.add_argument("--jsonl", action="store_true", help="Delete from JSONL repository only")
    args = parser.parse_args()
    
    if args.json:
        success = delete_project_json(args.project_id)
    elif args.jsonl:
        success = delete_project_jsonl(args.project_id)
    else:
        json_success = delete_project_json(args.project_id)
        jsonl_success = delete_project_jsonl(args.project_id)
        success = json_success and jsonl_success
    
    if not success:
        exit(1)

if __name__ == "__main__":
    main()