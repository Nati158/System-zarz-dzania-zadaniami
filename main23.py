class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nCompleted: {self.completed}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"Task {idx}:")
            print(task)
            print()

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_task(Task("Study for exam", "Prepare notes and review materials"))
    todo_list.add_task(Task("Buy groceries", "Milk, bread, eggs, vegetables"))
    todo_list.add_task(Task("Exercise", "Go for a run or do yoga"))
    todo_list.display_tasks()
