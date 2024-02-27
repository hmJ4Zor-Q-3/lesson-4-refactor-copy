import unittest

from src.Task import Task
from src.TaskManager import TaskManager


class TestTaskManager(unittest.TestCase):

    def test_add_task_1(self):
        tm = TaskManager()
        # verify manual adding
        i = 2
        a = "_Task_"
        tm.add_task(a, i)
        t = tm.find_task_by_id(i)
        self.assertEqual(t.identifier, i)
        self.assertEqual(t.description, a)
        # verify task manager picks the correct identifier
        b = "-task-"
        tm.add_task(b)
        i2 = 1
        t2 = tm.find_task_by_id(i2)
        self.assertEqual(t2.identifier, i2)
        self.assertEqual(t2.description, b)
        # verify no overwriting used identifier
        try:
            tm.add_task("desc", i2)
            self.assertTrue(False)
        except KeyError:
            self.assertTrue(True)

    def test_delete_task_1(self):
        tm = TaskManager()
        i = 2
        a = "89yw"
        tm._task_list[i] = Task(i, a)
        tm.delete_task(i)
        self.assertFalse(tm.contains_id(i))

    def test_find_task_by_id_1(self):
        tm = TaskManager()
        i = 901
        d = "2"
        tm._task_list[i] = Task(i, d)
        self.assertEqual(tm.find_task_by_id(i).description, d)

    def test_find_task_by_id_2(self):
        tm = TaskManager()
        ia = 758
        ib = -3
        ic = -2
        a = "243lop"
        b = "39402;'dsal"
        c = "aksoclllp23;"
        tm._task_list[ia] = Task(ia, a)
        tm._task_list[ib] = Task(ib, b)
        tm._task_list[ic] = Task(ic, c)
        self.assertEqual(tm.find_task_by_id(ib).description, b)
        self.assertNotEqual(tm.find_task_by_id(ic).description, b)
        self.assertEqual(tm.find_task_by_id(ia).description, a)

    def test_get_tasks_1(self):
        tm = TaskManager()
        ia = -239
        ib = 53000
        ic = 18
        a = "243lop"
        b = "39402;'dsal"
        c = "aksoclllp23;"
        tm._task_list[ia] = Task(ia, a)
        tm._task_list[ib] = Task(ib, b)
        tm._task_list[ic] = Task(ic, c)
        l = tm.get_tasks()
        self.assertEqual(l[0].identifier, ia)
        self.assertEqual(l[0].description, a)
        self.assertEqual(l[1].identifier, ib)
        self.assertEqual(l[1].description, b)
        self.assertEqual(l[2].identifier, ic)
        self.assertEqual(l[2].description, c)
        try:
            l[3]
            self.assertTrue(False)
        except IndexError:
            self.assertTrue(True)

    def test_renumber_tasks_1(self):
        tm = TaskManager()
        a = "a"
        b = "b"
        c = "c"
        tm._task_list[22] = Task(22, a)
        tm._task_list[3] = Task(3, b)
        tm._task_list[-9] = Task(-9, c)
        tm.renumber_tasks()
        self.assertEqual(tm.find_task_by_id(1).description, a)
        self.assertEqual(tm.find_task_by_id(2).description, b)
        self.assertEqual(tm.find_task_by_id(3).description, c)

    def test_update_task_1(self):
        tm = TaskManager()
        i = 1
        d = "090"
        tm._task_list[i] = Task(i, d)
        d2 = "Another Description"
        tm.update_task(i, d2)
        self.assertNotEqual(tm.find_task_by_id(i).description, d)
        self.assertEqual(tm.find_task_by_id(i).description, d2)

    def test_next_identifier_1(self):
        tm = TaskManager()
        d = "aLdo03"
        tm.add_task(d)
        self.assertEqual(tm.find_task_by_id(1).description, d)

    def test_next_identifier_2(self):
        tm = TaskManager()
        tm._task_list[0] = Task(0, "ssss")
        d = "aLdo03"
        tm.add_task(d)
        self.assertEqual(tm.find_task_by_id(1).description, d)

    def test_next_identifier_3(self):
        tm = TaskManager()
        tm._task_list[0] = Task(0, "fsf3")
        tm._task_list[2] = Task(2, "kldsakdl993_")

        d = ";l3p2"
        tm.add_task(d)
        self.assertEqual(tm.find_task_by_id(1).description, d)

        d2 = "' +-wlq'"
        tm.add_task(d2)
        self.assertEqual(tm.find_task_by_id(3).description, d2)
