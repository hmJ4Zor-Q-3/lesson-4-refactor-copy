from src.TaskManager import TaskManager
from src.io.JsonFileManager import JsonFileManager
from src.io.TaskManagerSerializer import TaskManagerSerializer


class TaskManagerConsoleUI:
    def __init__(self, path: str):
        """
        Creates a new task manager console interface.
        Args:
            path: the path to the file to load the task manager from.
            If no file is found a new empty task manager's used.
        """
        self._serializer = TaskManagerSerializer()
        self._file_manager = JsonFileManager(path)
        try:
            self._task_manager = self._serializer.read_json(self._file_manager.load_json())
        except FileNotFoundError:  # hidden to mirror original functionality more exactly, KeyError):
            self._task_manager = TaskManager()

    def main(self):
        """
        The entry point for running the interface.
        Returns: nothing.
        """
        while True:
            self.print_menu()
            if self.handle_choice(input("Choose an option: ")):
                break

    def print_menu(self):
        """
        Prints to the console the menu choice.
        Returns: nothing.
        """
        print("\nTask Manager")
        print("1. Add task")
        print("2. List tasks")
        print("3. Delete task")
        print("4. Update task")
        print("5. Exit")

    def handle_choice(self, choice: str):
        """
        Perform the behavior associated with a choice.
        Args:
            choice: a string representing the users chosen option.

        Returns: if the application was closed.
        """
        if choice == "1":
            self.add_task()
        elif choice == "2":
            self.list_tasks()
        elif choice == "3":
            self.delete_task()
        elif choice == "4":
            self.update_task()
        elif choice == "5":
            return True
        else:
            print("Invalid choice. Please choose a valid option.")
        return False

    def add_task(self):
        """
        Interface with user to add a task.
        Returns: nothing.
        """
        description = input("Enter a task: ")
        self._task_manager.add_task(description)
        self.save()
        print("Task added.")

    def list_tasks(self):
        """
        Lists all the tasks to the interface.
        Returns: nothing.
        """
        tasks = self._task_manager.get_tasks()
        if not tasks:
            print("No tasks.")
        else:
            for t in tasks:
                print(t)

    def delete_task(self):
        """
        Interface with user to delete a task.
        Returns: nothing.
        """
        self.list_tasks()
        task_id = int(input("Enter task ID to delete: "))
        if not self.validate_task_id(task_id):
            return

        self._task_manager.delete_task(task_id)
        print("Task deleted.")
        self._task_manager.renumber_tasks()
        self.save()

    def update_task(self):
        """
        Interface with user to update a task.
        Returns: nothing.
        """
        self.list_tasks()
        task_id = int(input("Enter task ID to update: "))
        if not self.validate_task_id(task_id):
            return

        new_task = input("Enter new task: ")
        self._task_manager.update_task(task_id, new_task)
        print("Task updated.")
        self.save()

    def save(self):
        """
        Writes the contents to the active file.
        Returns: nothing.
        """
        self._file_manager.save_json(self._serializer.write_json(self._task_manager))

    def validate_task_id(self, identifier: int):
        """
        Tests if an identifier can be used.
        Args:
            identifier: the identifier to be tested.

        Returns: if the identifier was unused.
        """
        if self._task_manager.contains_id(identifier):
            return True
        else:
            print("Invalid task ID.")
            return False
