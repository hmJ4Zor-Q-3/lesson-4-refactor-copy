import json
import unittest

from src.Task import Task
from src.io.TaskSerializer import TaskSerializer


class TestTaskSerializer(unittest.TestCase):

    def test_conversion_1(self):
        i = -102
        d = "ddasd"
        t = Task(i, d)
        ts = TaskSerializer()
        t2 = ts.read_json(ts.write_json(t))

        self.assertIsInstance(t2, Task)

        self.assertEqual(t.identifier, t2.identifier)
        self.assertEqual(t.description, t2.description)

    def test_conversion_2(self):
        i = -102
        d = ""
        t = Task(i, d)
        ts = TaskSerializer()
        t2 = ts.read_json(ts.write_json(t))

        self.assertIsInstance(t2, Task)

        self.assertEqual(t.identifier, t2.identifier)
        self.assertEqual(t.description, t2.description)

    def test_conversion_3(self):
        i = -102
        d = "ddasd"
        t = Task(i, d)
        ts = TaskSerializer()
        t2 = ts.read_json(json.loads(json.dumps(ts.write_json(t))))

        self.assertIsInstance(t2, Task)

        self.assertEqual(t.identifier, t2.identifier)
        self.assertEqual(t.description, t2.description)
