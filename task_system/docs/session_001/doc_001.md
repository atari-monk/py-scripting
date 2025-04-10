# Idea Agent Coder

## Task Model

I need a JSON model that will define a task for the coder agent to implement.  
Let's start with a simple model that we can gradually expand.

- Let's begin with this:

```json
{
	"task": {
		"id": "unique_task_identifier",
		"title": "Brief descriptive title of the task",
		"description": "Detailed description of what needs to be implemented",
		"requirements": [
			"List of specific requirements",
			"Expected functionality",
			"Any constraints"
		],
		"input": {
			"description": "Description of expected input if applicable",
			"examples": []
		},
		"output": {
			"description": "Description of expected output",
			"examples": []
		},
		"language": "programming_language",
		"difficulty": "easy/medium/hard",
		"tags": ["list", "of", "relevant", "tags"],
		"created_at": "timestamp",
		"updated_at": "timestamp"
	}
}
```

## API

Could we build a Python system to create these tasks?  
What I mean by this is:  
Let's assume I'm an agent and the system asks me questions until the task is fully generated.  
We can then use machines as agents as well.  
We can use Python FastAPI as the technology.  
Let's assume there are mandatory questions that need to be answered.  
Then we can display a list of optional ones so the user can fill them in until they're satisfied.

Perhaps we need a CLI script that will handle the dialog with the user but then use the API to store the final result precisely. That seems like a reasonable approach, unless you have better ideas—don't hesitate to suggest them.
