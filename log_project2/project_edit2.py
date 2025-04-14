import logging
import argparse
from shared_library.input_validator import InputValidator
from log_project2.crud.ProjectCRUD import ProjectCRUD
from log_project2.crud.ProjectCRUDJsonl import ProjectCRUDJsonl

logger = logging.getLogger(__name__)

def edit_project_json(project_id: int, data: dict, repository: ProjectCRUD) -> bool:
    return repository.update_by_id(project_id, **data)

def edit_project_jsonl(project_id: int, data: dict, repository: ProjectCRUDJsonl) -> bool:
    return repository.update_by_id(project_id, **data)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Edit an existing project. Specify the project ID and fields to update.")
    parser.add_argument("project_id", type=int, help="ID of the project to edit")
    parser.add_argument("field_value_pairs", nargs="+", help="Field-value pairs to update (format: field=value)")
    return parser.parse_args()

def main():
    args = parse_arguments()
    project_id = args.project_id
    field_value_pairs = args.field_value_pairs

    json_repository = ProjectCRUD()
    jsonl_repository = ProjectCRUDJsonl()

    project_existing = json_repository.get_by_id(project_id)
    if not project_existing:
        logger.error(f"Project with ID '{project_id}' not found.")
        return

    data_input = InputValidator.validate_and_parse(field_value_pairs)
    if not data_input:
        return

    try:
        json_result = edit_project_json(project_id, data_input, json_repository)
        jsonl_result = edit_project_jsonl(project_id, data_input, jsonl_repository)

        if json_result and jsonl_result:
            logger.info(f"Project '{project_id}' updated successfully in both repositories (JSON and JSONL).")
        else:
            if not json_result:
                logger.warning(f"Failed to update project '{project_id}' in JSON repository.")
            if not jsonl_result:
                logger.warning(f"Failed to update project '{project_id}' in JSONL repository.")
    except Exception as e:
        logger.error(f"Unexpected error during project update: {e}")

if __name__ == "__main__":
    main()