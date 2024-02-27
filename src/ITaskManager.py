from abc import ABC, abstractmethod
from typing import List

from src.Task import Task


class ITaskManager(ABC):
    @abstractmethod
    def add_task(self, description: str, identifier: int = None):
        """
        Adds in a new task.
        Args:
            description: the description for the task to add.
            identifier: optional, the identifier to add the task under,
            should throw an error if already used. If unspecified identifier is chosen by the task manager

        Returns: nothing.
        """
        pass

    @abstractmethod
    def contains_id(self, task_id) -> bool:
        """
        Checks if a task by an identifier is managed
        Args:
            task_id: the identifier to test if is used.

        Returns: if a task by that given identifier is managed
        """
        pass

    @abstractmethod
    def delete_task(self, task_id: int):
        """
        Deletes a task from the task manager.
        Args:
            task_id: the identifier of the task to delete.

        Returns: nothing.
        """
        pass

    @abstractmethod
    def find_task_by_id(self, task_id: int) -> Task:
        """
        Finds a given task by it's identifier.
        Args:
            task_id: the identifier of the task to find.

        Returns: the found task.
        """
        pass

    @abstractmethod
    def get_tasks(self) -> List:
        """
        Gets a list holding all the currently managed tasks,
        ordering shouldn't change across calls,
        shouldn't be a gateway to modifying the tasks managed.
        Returns: a list of all the current tasks.
        """
        pass

    @abstractmethod
    def renumber_tasks(self):
        """
        Updates the identifiers of all managed tasks, starting with one and increasing by one in order.
        Returns: nothing.
        """
        pass

    @abstractmethod
    def update_task(self, task_id: int, new_description: str):
        """
        Updates the description of a specific task.
        Args:
            task_id: the identifier of the task to update.
            new_description: the new description for the specified task.

        Returns: nothing.
        """
        pass
