from task_system.api.models import get_language_list

try:
    languages = get_language_list()
    result = "Language must be one of: " + ", ".join(languages)
    expected_result = "Language must be one of: python, javascript, java, csharp, typescript, c++, powershell, markdown, other"
    
    if result == expected_result:
        print("SUCCESS! Validation worked")
    else:
        raise ValueError(f"Validation failed. Expected: '{expected_result}', got: '{result}'")

except Exception  as e:
    print(f"FAILED: {e}")