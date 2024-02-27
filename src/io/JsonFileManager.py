import json

class JsonFileManager:
    def __init__(self, path: str):
        """
        A wrapper for reading and writing JSON to/from a file.
        Args:
            path: the path of the file to manage:
        """
        self._path = path

    def load_json(self) -> str:
        """
        Loads the contents of the file into an equivalent json representation
        Returns: the file contents translated to an object.
        """
        with open(self._path, "r") as f:
            return json.load(f)

    def save_json(self, data):
        """
        Saves an object as a json representation at the managed file
        Args:
            data: the object to be written.

        Returns: nothing.
        """
        with open(self._path, "w") as f:
            json.dump(data, f)
