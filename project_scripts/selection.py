import random

projects = ["py_scripting"]

decision_methods = {}

def register_method(func):
    decision_methods[func.__name__] = func
    return func

@register_method
def priority_based():
    priorities = {
        "py_scripting": 1,
    }
    return min(projects, key=lambda p: priorities.get(p, float('inf')))

@register_method
def random_choice():
    return random.choice(projects)

@register_method
def longest_idle():
    last_worked = {
        "py_scripting": 0
    }
    return max(projects, key=lambda p: last_worked.get(p, 0))

def decide_project(method_name="random_choice"):
    if method_name not in decision_methods:
        raise ValueError(f"Method '{method_name}' not found. Available methods: {list(decision_methods.keys())}")
    return decision_methods[method_name]()

def main() :
    chosen_method = "priority_based"
    project = decide_project(chosen_method)
    print(f"Selected project to work on: {project} (using '{chosen_method}' method)")

if __name__ == "__main__":
    main()