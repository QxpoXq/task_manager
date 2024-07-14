import argparse
import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({'description': description, 'done': False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        status = '✓' if task['done'] else '✗'
        print(f"{i}. [{status}] {task['description']}")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)
        print(f"Completed task: {tasks[index]['description']}")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {task['description']}")
    else:
        print("Invalid task number.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager")
    parser.add_argument('command', choices=['add', 'list', 'complete', 'delete'])
    parser.add_argument('args', nargs='*')
    args = parser.parse_args()

    if args.command == 'add':
        add_task(' '.join(args.args))
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'complete':
        complete_task(int(args.args[0]) - 1)
    elif args.command == 'delete':
        delete_task(int(args.args[0]) - 1)

if __name__ == "__main__":
    main()
