import runner
from unittest import TestCase

class RunnerTest(TestCase):

    def test_walk(self):
        Run = runner.Runner('Oleg')
        for i in range(10):
            Run.walk()
        self.assertEqual(Run.distance, 50)

    def test_run(self):
        Run = runner.Runner('Kate')
        for i in range(10):
            Run.run()
        self.assertEqual(Run.distance, 100)

    def test_challenge(self):
        Run1 = runner.Runner('Vasya')
        Run2 = runner.Runner('Vera')
        for i in range(10):
            Run1.walk()
            Run2.run()
        self.assertNotEqual(Run1.distance, Run2.distance)



if __name__ == '__main__':
    unittest.main()



