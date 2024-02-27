import unittest

from src.Task import Task


class TestTask(unittest.TestCase):

    def test_init_1(self):
        i = 123
        d = "deskc"
        t = Task(i, d)
        self.assertEqual(t.identifier, i)
        self.assertEqual(t.description, d)

    def test_description_mutation(self):
        d = "desk32c"
        t = Task(0, d)
        self.assertEqual(t.description, d)
        d2 = "A more english language description."
        t.description = d2
        self.assertEqual(t.description, d2)

    def test_identifier_immutability(self):
        i = -1
        t = Task(i, "base 2 s")
        self.assertEqual(t.identifier, i)
        try:
            t.identifier = 1
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)

        self.assertEqual(t.identifier, i)
