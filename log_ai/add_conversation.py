import argparse
from pydantic import ValidationError
from log_ai.crud.conversation_crud import ConversationCRUD
from log_ai.crud.dialogue_crud import DialogueCRUD
from log_ai.model.conversation import Conversation

def add_conversation(name, description):
    try:
        validated_conversation = Conversation(
            name=name,
            description=description
        )
    except ValidationError as e:
        print("Error: Invalid input data.")
        print(e.json())
        return

    conversation_crud = ConversationCRUD()
    try:
        result = conversation_crud.create(
            name=validated_conversation.name,
            description=validated_conversation.description,
            start_timestamp=validated_conversation.start_timestamp,
            last_mod_timestamp=validated_conversation.last_mod_timestamp
        )
        if result:
            print(f"Conversation '{result['name']}' created successfully with id '{result['id']}'.")
        else:
            print("Failed to create conversation.")
    except Exception as e:
        print(f"Unexpected error during conversation creation: {e}")

def edit_conversation(conversation_id, name, description):
    conversation_crud = ConversationCRUD()
    existing_conversation = conversation_crud.read(conversation_id)
    if not existing_conversation:
        print(f"Error: Conversation with ID '{conversation_id}' not found.")
        return

    if name != "none":
        existing_conversation['name'] = name
    if description != "none":
        existing_conversation['description'] = description

    try:
        validated_conversation = Conversation(
            name=existing_conversation['name'],
            description=existing_conversation['description'],
            start_timestamp=existing_conversation['start_timestamp'],
            last_mod_timestamp=existing_conversation['last_mod_timestamp']
        )
    except ValidationError as e:
        print("Error: Invalid input data.")
        print(e.json())
        return

    try:
        result = conversation_crud.update(
            conversation_id,
            **validated_conversation.model_dump()
        )
        if result:
            print(f"Conversation '{conversation_id}' updated successfully.")
        else:
            print("Failed to update conversation.")
    except Exception as e:
        print(f"Unexpected error during conversation update: {e}")

def delete_conversation(conversation_id):
    conversation_crud = ConversationCRUD()
    dialogue_crud = DialogueCRUD()
    
    existing_conversation = conversation_crud.read(conversation_id)
    if not existing_conversation:
        print(f"Error: Conversation with ID '{conversation_id}' not found.")
        return

    dialogs = dialogue_crud.get_dialogs_by_conversation_id(conversation_id)
    if dialogs:
        print(f"Error: Conversation with ID '{conversation_id}' has associated dialogs and cannot be deleted.")
        return

    try:
        result = conversation_crud.delete(conversation_id)
        if result:
            print(f"Conversation '{conversation_id}' deleted successfully.")
        else:
            print(f"Failed to delete conversation '{conversation_id}'.")
    except Exception as e:
        print(f"Unexpected error during conversation deletion: {e}")

def main():
    parser = argparse.ArgumentParser(description="Add, edit, or delete a conversation.")
    subparsers = parser.add_subparsers(dest='action', required=True)

    # Add command
    add_parser = subparsers.add_parser('add', help='Create a new conversation')
    add_parser.add_argument('name', help='Name of the conversation')
    add_parser.add_argument('description', help='Description of the conversation')

    # Edit command
    edit_parser = subparsers.add_parser('edit', help='Edit an existing conversation')
    edit_parser.add_argument('conversation_id', help='ID of the conversation to edit')
    edit_parser.add_argument('name', help='New name or "none" to keep current')
    edit_parser.add_argument('description', help='New description or "none" to keep current')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a conversation')
    delete_parser.add_argument('conversation_id', help='ID of the conversation to delete')

    args = parser.parse_args()

    if args.action == 'add':
        add_conversation(args.name, args.description)
    elif args.action == 'edit':
        edit_conversation(args.conversation_id, args.name, args.description)
    elif args.action == 'delete':
        delete_conversation(args.conversation_id)

if __name__ == '__main__':
    main()