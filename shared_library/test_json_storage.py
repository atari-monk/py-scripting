import pytest
import json
import os
from shared_library.json_file_storage import JSONFileStorage

@pytest.fixture
def setup_and_teardown():
    test_file = 'test_data.json'
    if os.path.exists(test_file):
        os.remove(test_file)
    
    yield test_file
    
    if os.path.exists(test_file):
        os.remove(test_file)

def test_initial_file_creation(setup_and_teardown):
    test_file = setup_and_teardown
    storage = JSONFileStorage(test_file)
    
    assert os.path.exists(test_file)

    with open(test_file, 'r') as f:
        data = json.load(f)
        assert data == []

def test_read_data_empty(setup_and_teardown):
    test_file = setup_and_teardown
    storage = JSONFileStorage(test_file)
    data = storage.load_all ()
    assert data == []

def test_write_data(setup_and_teardown):
    test_file = setup_and_teardown
    storage = JSONFileStorage(test_file)
    data_to_write = [{"key": "value"}]

    storage.save_all(data_to_write)

    with open(test_file, 'r') as f:
        data = json.load(f)
        assert data == data_to_write

def test_write_and_read_multiple_entries(setup_and_teardown):
    test_file = setup_and_teardown
    storage = JSONFileStorage(test_file)
    data_to_write = [{"key": "value1"}, {"key": "value2"}]

    storage.save_all(data_to_write)

    data = storage.load_all ()
    assert data == data_to_write

def test_read_data_with_invalid_json(setup_and_teardown):
    test_file = setup_and_teardown
    with open(test_file, 'w') as f:
        f.write("{invalid json}")

    storage = JSONFileStorage(test_file)
    data = storage.load_all ()
    
    assert data == []

def test_write_data_error_handling(setup_and_teardown):
    test_file = setup_and_teardown
    storage = JSONFileStorage(test_file)
    data_to_write = [{"key": "value"}]
    storage.save_all(data_to_write)

    os.chmod(test_file, 0o444)

    storage.save_all(data_to_write)

    with open(test_file, 'r') as f:
        data = json.load(f)
        assert data == data_to_write

    os.chmod(test_file, 0o666)
