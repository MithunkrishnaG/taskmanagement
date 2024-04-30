# task_manager.py
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def list_tasks(self):
        for task in self.tasks:
            task.display_details()
            print()

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.status}\n")

    def load_tasks(self, filename):
        self.tasks = []
        with open(filename, 'r') as file:
            for line in file:
                title, description, due_date, status = line.strip().split(',')
                task = Task(title, description, due_date)
                task.update_status(status)
                self.tasks.append(task)
