import logging
import argparse
from typing import Dict, Any, List
from log_project.project import Project
from log_project.project_crud import ProjectCRUD, ProjectCRUD3

logger = logging.getLogger(__name__)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Edit an existing project. Specify the project ID and fields to update.")
    parser.add_argument("project_id", type=int, help="ID of the project to edit")
    parser.add_argument("updates", nargs="+", help="Field updates in format field=value")
    return parser.parse_args()

def validate_updates(field_value_pairs: List[str]) -> Dict[str, Any]:
    update_data = {}
    for field_value in field_value_pairs:
        if "=" not in field_value:
            raise ValueError(f"Invalid format for '{field_value}', expected 'field=value'")

        field, value = map(str.strip, field_value.split("=", 1))
        field = field.lower()
        parsed_value = Project.parse_fields(field, value)
        update_data[field] = parsed_value
    return update_data

def edit_project_json(project_id: int, update_data: Dict[str, Any]) -> bool:
    repository = ProjectCRUD()
    existing_project = repository.get_by_id(project_id)
    if not existing_project:
        logger.error(f"Project with ID '{project_id}' not found.")
        return False
    return repository.update_by_id(project_id, **update_data)

def edit_project_jsonl(project_id: int, update_data: Dict[str, Any]) -> bool:
    repository = ProjectCRUD3()
    existing_project = repository.get_by_id(project_id)
    if not existing_project:
        logger.error(f"Project with ID '{project_id}' not found.")
        return False
    return repository.update_by_id(project_id, **update_data)

def main():
    args = parse_arguments()
    
    try:
        update_data = validate_updates(args.updates)
        
        json_success = edit_project_json(args.project_id, update_data)
        jsonl_success = edit_project_jsonl(args.project_id, update_data)
        
        if json_success and jsonl_success:
            logger.info(f"Project '{args.project_id}' updated successfully in both repositories (JSON and JSONL).")
        else:
            if not json_success:
                logger.warning(f"Failed to update project '{args.project_id}' in JSON repository.")
            if not jsonl_success:
                logger.warning(f"Failed to update project '{args.project_id}' in JSONL repository.")
    except ValueError as e:
        logger.error(str(e))
    except Exception as e:
        logger.error(f"Unexpected error during project update: {e}")

if __name__ == "__main__":
    main()