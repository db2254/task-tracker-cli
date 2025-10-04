import argparse
import json
from pathlib import Path
from datetime import datetime

# Path to store the tasks
TASKS_FILE = Path("tasks.json")

def load_tasks():
    """Load tasks from the JSON file, or return empty list if not exist"""
    if not TASKS_FILE.exists():
        return[]
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks list to JSON file"""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

# Functions

def add_task(args):
    tasks = load_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1

    now = datetime.now().isoformat()
    new_task = {
        "id": new_id,
        "description": args.description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")


def list_tasks(args):
    filter_status = args.status if args.status else "None"
    print(f"Running list with filter: {filter_status}")

def update_task(args):
    print(f"Running update on task {args.id} with new description: {args.new_description}")

def delete_task(args):
    print(f"Running delete on task {args.id}")


def main():
    parser = argparse.ArgumentParser(
        description="Task Tracker CLI - Manage your tasks from the command line"
    )

    subparsers = parser.add_subparsers(
        title="Commands",
        dest="Command",
        required=True,
        help="Available commands"
    )


    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")
    parser_add.set_defaults(func=add_task)

    # List command
    parser_list = subparsers.add_parser("list",  help="List tasks")
    parser_list.add_argument(
        "status", type=str, nargs="?", choices=["todo", "in-progress", "done"],
        help="Optional filter by task status"
    )
    parser_list.set_defaults(func=list_tasks)

    # Update command
    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("id", type=int, help="Task ID")
    parser_update.add_argument("new_description", type=str, help="New description")
    parser_update.set_defaults(func=update_task)

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID")
    parser_delete.set_defaults(func=delete_task)

    # Parse arguments and call the correct function
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()