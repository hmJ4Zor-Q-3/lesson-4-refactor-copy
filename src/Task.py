class Task:
    """
    A representation of a uniquely identified task.
    """

    def __init__(self, identifier: int, description: str):
        """
        The object initializer.

        Args:
            identifier: a unique identifier referencing this particular task, usually an integer, usually not changed.
            description: a description of the task, usually a string, can be changed
        """
        self._identifier = identifier
        self.description = description

    def __str__(self):
        return f"{self._identifier}. {self.description}"

    @property
    def identifier(self):
        return self._identifier
