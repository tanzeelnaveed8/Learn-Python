import click
import json
import os

TodoFile = 'todo.json'

def loadtasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist"""
    if not os.path.exists(TodoFile):
        return []
    with open(TodoFile, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TodoFile, 'w') as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """A simple TodoList Manager"""
    pass

@click.command()
@click.argument('task')
def add(task):
    """Add a new task to the list"""
    tasks = loadtasks()
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")

@click.command()
def list():
    """List all tasks"""
    tasks = loadtasks()
    if not tasks:
        click.echo("No tasks found")
        return
    for i, task in enumerate(tasks, 1):
        status = '✅' if task['done'] else '❌'
        click.echo(f"{i}. {task['task']} - {status}")

@click.command()
@click.argument('task_number', type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks = loadtasks()
    try:
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as complete")
    except IndexError:
        click.echo("Invalid task number")

@click.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Delete a task"""
    tasks = loadtasks()
    try:
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task {task['task']} deleted successfully")
    except IndexError:
        click.echo("Invalid task number")

# Add commands to the CLI
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)  # Fixed spelling
cli.add_command(delete)

if __name__ == '__main__':
    cli()
