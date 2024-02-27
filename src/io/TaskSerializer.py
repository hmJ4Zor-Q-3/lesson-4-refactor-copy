from src.Task import Task


class TaskSerializer:
    """
    A class for converting tasks to/from other formats.
    """
    IDENTIFIER_KEY = "identifier"
    DESCRIPTION_KEY = "description"

    def write_json(self, task: Task):
        """
        Writes a task as a well translatable json representation.
        Args:
            task: the task to be serialized.

        Returns: A well translatable object representing the json representation of the task.
        """
        return {TaskSerializer.IDENTIFIER_KEY: task.identifier,
                TaskSerializer.DESCRIPTION_KEY: task.description}

    def read_json(self, data) -> Task:
        """
        Reads a task from a json representation.
        Args:
            data: a dictionary or similar strongly representing a task object,
            must be equivalently formatted to the output of write_json.

        Returns: a task that was represented by the input object.
        """
        return Task(data[TaskSerializer.IDENTIFIER_KEY], data[TaskSerializer.DESCRIPTION_KEY])

    # def write_json_s(self, task: Task):
    #     """
    #     Writes a task to a json string.
    #     Args:
    #         task: the task to be serialized.
    #
    #     Returns: A json syntax string representing the task
    #     """
    #     return json.dumps(self.write_json(task))
    #
    # def read_json_s(self, data):
    #     """
    #     Reads a task from a json string.
    #     Args:
    #         data: a string or similar representing a json object representing a task.
    #
    #     Returns: a task that was represented by the input string.
    #     """
    #     return self.read_json(json.loads(data))
