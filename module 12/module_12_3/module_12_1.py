import runner
from unittest import TestCase
import unittest

class RunnerTest(TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'не повезло')
    def test_walk(self):
        Run = runner.Runner('Oleg')
        for i in range(10):
            Run.walk()
        self.assertEqual(Run.distance, 50)

    @unittest.skipIf(is_frozen, 'не повезло')
    def test_run(self):
        Run = runner.Runner('Kate')
        for i in range(10):
            Run.run()
        self.assertEqual(Run.distance, 100)

    @unittest.skipIf(is_frozen, 'не повезло')
    def test_challenge(self):
        Run1 = runner.Runner('Vasya')
        Run2 = runner.Runner('Vera')
        for i in range(10):
            Run1.walk()
            Run2.run()
        self.assertNotEqual(Run1.distance, Run2.distance)



if __name__ == '__main__':
    unittest.main()



