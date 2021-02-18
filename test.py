import unittest

from programGUIClass import programGUI


class TestFileClose(unittest.TestCase):
    def testFileClose(self):
        with self.assertRaises(TypeError):
            gui2 = programGUI(self, True)
            gui2.run()


class TestGUI(unittest.TestCase):
    def testRun(self):
        gui = programGUI(False)
        result = gui.run()
        self.assertEqual(result, 1)


if __name__ == "__main__":

    unittest.main()
