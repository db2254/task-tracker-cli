# Task Tracker CLI

A simple command-line tool to track and manage your tasks.  
— supporting commands like **add**, **list**, **update**, and **delete**.

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
```
### 2. Create and activate a virtual environment
```
python -m venv .venv
# Activate (PowerShell)
.\.venv\Scripts\Activate.ps1
```
### 3. Run the CLI
```
python task_cli.py --help
```

### Available Commands

### Add a task
```
python task_cli.py add "Buy groceries"
```
### List all tasks (or filter by status)
```
python task_cli.py list
python task_cli.py list done
```
### Update a task
```
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task
```
python task_cli.py delete 1
```
### Set task status (in-progress, done)
```
python task_cli.py done 2

python task_cli.py mark-in-progress 2

python task_cli.py list
```


### Technologies used

Python

argparse(built-in module)
