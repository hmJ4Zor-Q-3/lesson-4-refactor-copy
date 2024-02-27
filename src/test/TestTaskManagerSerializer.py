import json
import unittest

from src.ITaskManager import ITaskManager
from src.TaskManager import TaskManager
from src.io.TaskManagerSerializer import TaskManagerSerializer


class TestTaskSerializer(unittest.TestCase):

    def test_conversion_1(self):
        ts = [(1, "809dsauj"), (4, "l34"), (0, "d2k")]
        tm = TaskManager()
        for t in ts:
            tm.add_task(t[1], t[0])

        tms = TaskManagerSerializer()
        tm2 = tms.read_json(tms.write_json(tm))

        self.assertIsInstance(tm2, ITaskManager)
        self.equivalence_test(tm, tm2)

    def test_conversion_2(self):
        ts = [(31, "l"), (10, "ftrygvbhj n"), (9, "k")]
        tm = TaskManager()
        for t in ts:
            tm.add_task(t[1], t[0])

        tms = TaskManagerSerializer()
        tm2 = tms.read_json(json.loads(json.dumps(tms.write_json(tm))))

        self.assertIsInstance(tm2, ITaskManager)
        self.equivalence_test(tm, tm2)

    def equivalence_test(self, tm1, tm2):
        tml = tm1.get_tasks()
        tml2 = tm2.get_tasks()
        self.assertEqual(len(tml), len(tml2))
        for i in range(len(tml)):
            t = tml[i]
            t2 = tml2[i]
            self.assertEqual(t.identifier, t2.identifier)
            self.assertEqual(t.description, t2.description)