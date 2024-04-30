# main.py
from task import Task
from task_manager import TaskManager

if __name__ == "__main__":
    task_manager = TaskManager()

    # Example usage
    task1 = Task("Complete project", "Finish the coding project", "2024-03-15")
    task2 = Task("Study for exam", "Prepare for the upcoming exam", "2024-03-10")

    task_manager.add_task(task1)
    task_manager.add_task(task2)

    print("List of tasks:")
    task_manager.list_tasks()

    task_manager.save_tasks("tasks.txt")

    # Load tasks from file
    task_manager.load_tasks("tasks.txt")

    print("\nAfter loading tasks:")
    task_manager.list_tasks()
