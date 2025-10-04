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

# Main Functions


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
    tasks = load_tasks()
    if not tasks:
        print("No tasks found")
        return
    
    if args.status:
        tasks = [t for t in tasks if t["status"] == args.status]
    
    if not tasks:
        print(f"No tasks found with status: {args.status}")
        return
    
    print(f"\n Listing {len(tasks)} task(s):\n")
    for task in tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']})")
        print(f"    Created: {task['createdAt']}")
        print(f"    Updated: {task['updatedAt']}\n")


def update_task(args):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == args.id), None)
    if not task:
        print(f"Task with ID {args.id} not found.")
        return
    
    task["description"] = args.new_description
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task {args.id} updated successfully")
   

def delete_task(args):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == args.id), None)
    if not task:
        print(f"Task with ID {args.id} not found.")
        return
    
    tasks = [t for t in tasks if t["id"] != args.id]
    save_tasks(tasks)
    print(f"Task {args.id} deleted successfully")


def mark_in_progress_task(args):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == args.id), None)
    if not task:
        print(f"Task with {args.id} not found.")
        return
    
    task["status"] = "in-progress"
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task {args.id} marked as in progress.")


def mark_done_task(args):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == args.id), None)
    if not task:
        print(f"Task with {args.id} not found.")
        return
    
    task["status"] = "done"
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task {args.id} marked as done.")


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

    # mark in progress command
    parser_mark_in_progress = subparsers.add_parser(
        "mark-in-progress",
        help="Mark a task as in-progress"
    )
    parser_mark_in_progress.add_argument("id", type=int, help="Task ID")
    parser_mark_in_progress.set_defaults(func=mark_in_progress_task)

    # Done command
    parser_done = subparsers.add_parser(
        "done",
        help="Mark a task as done"
    )
    parser_done.add_argument("id", type=int, help="Task ID")
    parser_done.set_defaults(func=mark_done_task)

    # Parse arguments and call the correct function
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
