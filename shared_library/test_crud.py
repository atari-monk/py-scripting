import pytest
from unittest.mock import MagicMock
from shared_library.json_repository import JSONRepository

class ItemModel:
    def __init__(self, name: str, description: str):
        if not name or not description:
            raise ValueError("Both 'name' and 'description' are required.")
        self.name = name
        self.description = description
        self.id = None

    def to_dict(self):
        return {"name": self.name, "description": self.description, "id": self.id}

@pytest.fixture
def mock_storage():
    mock = MagicMock()
    mock.read_data.return_value = []
    return mock

@pytest.fixture
def crud(mock_storage):
    return JSONRepository(dict, mock_storage)

def test_create(crud, mock_storage):
    data = {"name": "Item 1", "description": "A test item"}
    
    result = crud.create(**data)
    
    assert result is not None
    assert result["name"] == "Item 1"
    assert result["description"] == "A test item"
    assert result["id"] == 1

    mock_storage.write_data.assert_called_once_with([result])

def test_read(crud, mock_storage):
    item_data = {"id": 1, "name": "Item 1", "description": "A test item"}
    mock_storage.read_data.return_value = [item_data]
    
    result = crud.read(1)
    
    assert result is not None
    assert result["name"] == "Item 1"
    assert result["description"] == "A test item"

def test_update(crud, mock_storage):
    item_data = {"id": 1, "name": "Item 1", "description": "A test item"}
    mock_storage.read_data.return_value = [item_data]
    
    updated_data = {"name": "Updated Item 1", "description": "Updated description"}
    result = crud.update(1, **updated_data)
    
    assert result is True
    assert item_data["name"] == "Updated Item 1"
    assert item_data["description"] == "Updated description"
    
    mock_storage.write_data.assert_called_once_with([item_data])

def test_delete(crud, mock_storage):
    item_data = {"id": 1, "name": "Item 1", "description": "A test item"}
    mock_storage.read_data.return_value = [item_data]
    
    result = crud.delete(1)
    
    assert result is True
    mock_storage.write_data.assert_called_once_with([])

def test_list_all(crud, mock_storage):
    item_data_1 = {"id": 1, "name": "Item 1", "description": "A test item"}
    item_data_2 = {"id": 2, "name": "Item 2", "description": "Another item"}
    mock_storage.read_data.return_value = [item_data_1, item_data_2]
    
    result = crud.list_all()
    
    assert len(result) == 2
    assert result[0]["name"] == "Item 1"
    assert result[1]["name"] == "Item 2"

def test_update_item_not_found(crud, mock_storage):
    mock_storage.read_data.return_value = []
    
    result = crud.update(999, name="Non-existent Item")
    
    assert result is False
    mock_storage.write_data.assert_not_called()
