import os
import json

def list_tasks(tasks):
    print()
    if not tasks:
        print('No tasks in the list')
        return

    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')
    print()


def undo(tasks, tasks_redo):
    print()
    if not tasks:
        print('No tasks to undo')
        return

    task = tasks.pop()
    print(f'{task=} removed from the task list.')
    tasks_redo.append(task)
    print()
    list_tasks(tasks)


def redo(tasks, tasks_redo):
    print()
    if not tasks_redo:
        print('No tasks to redo')
        return

    task = tasks_redo.pop()
    print(f'{task=} added back to the task list.')
    tasks.append(task)
    print()
    list_tasks(tasks)


def add_task(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('You did not type a task')
        return

    print(f'{task=} added to the task list.')
    tasks.append(task)
    print()
    list_tasks(tasks)


# LOAD
tasks = []
tasks_redo = []

try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    pass
except json.JSONDecodeError:
    pass


# MAIN LOOP
while True:
    print('Commands: list, undo, redo')
    user_input = input('Enter a task or command: ')

    commands = {
        'list': lambda: list_tasks(tasks),
        'undo': lambda: undo(tasks, tasks_redo),
        'redo': lambda: redo(tasks, tasks_redo),
        'clear': lambda: os.system('clear'),
        'add': lambda: add_task(user_input, tasks),
    }

    command = commands.get(user_input) if commands.get(user_input) is not None else commands['add']
    command()

    # SAVE
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)