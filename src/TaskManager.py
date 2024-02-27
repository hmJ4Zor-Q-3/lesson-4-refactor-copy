from typing import List

from src.ITaskManager import ITaskManager
from src.Task import Task


class TaskManager(ITaskManager):

    def __init__(self):
        self._task_list = {}

    def add_task(self, description: str, identifier: int = None):
        i = self.next_identifier() if identifier is None else identifier
        if self.contains_id(i):
            raise KeyError(f"The identifier {i}'s already used.")
        self._task_list[i] = (Task(i, description))

    def contains_id(self, task_id) -> bool:
        return self._task_list.__contains__(task_id)

    def delete_task(self, task_id: int):
        del self._task_list[task_id]

    def find_task_by_id(self, task_id: int) -> Task:
        return self._task_list[task_id]

    def get_tasks(self) -> List:
        return [x for x in self._task_list.values()]

    def renumber_tasks(self):
        updated_list = []
        i = 1
        for t in self._task_list.values():
            updated_list.append(Task(i, t.description))
            i += 1

        self._task_list.clear()
        for t in updated_list:
            self._task_list[t.identifier] = t

    def update_task(self, task_id: int, new_description: str):
        self._task_list[task_id].description = new_description

    def next_identifier(self):
        """
        Gets a free integer identifier.
        Returns: The lowest free integer identifier greater than or equal to one.
        """
        i = 1
        while True:
            if self.contains_id(i):
                i = i + 1
            else:
                return i
