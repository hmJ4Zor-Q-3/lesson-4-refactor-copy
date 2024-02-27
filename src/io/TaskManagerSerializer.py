from src.ITaskManager import ITaskManager
from src.TaskManager import TaskManager
from src.io.TaskSerializer import TaskSerializer


class TaskManagerSerializer:
    """
    A class for converting general case ITaskManager to/from other formats.
    """
    TASKS_KEY = "tasks"

    def __init__(self):
        self._task_serializer = TaskSerializer()

    def write_json(self, task_manager: ITaskManager):
        """
        Writes a ITaskManager as a well translatable json representation.
        Args:
            task_manager: the ITaskManager to be serialized.

        Returns: A well translatable object representing the json representation of the ITaskManager.
        """

        return {TaskManagerSerializer.TASKS_KEY:
                    [self._task_serializer.write_json(x) for x in task_manager.get_tasks()]}

    def read_json(self, data) -> TaskManager:
        """
        Reads a ITaskManager from a json representation.
        Args:
            data: a dictionary or similar strongly representing a ITaskManager object,
            must be equivalently formatted to the output of write_json.

        Returns: a TaskManager that was represented by the input object.
        """
        tm = TaskManager()
        for t in data[TaskManagerSerializer.TASKS_KEY]:
            tm.add_task(t[TaskSerializer.DESCRIPTION_KEY], t[TaskSerializer.IDENTIFIER_KEY])
        return tm
