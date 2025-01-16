from HumanMoveTest import Runner
from unittest import TestCase
import unittest
import logging

class RunnerTest(TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'не повезло')
    def test_walk(self):
        try:
            run = Runner('Oleg', -1)
            for i in range(10):
                run.walk()
            logging.info(f'test_walk выполнен успешно')
            self.assertEqual(run.distance, 100)
        except ValueError:
            logging.error(f'Неверная скорость для runner')

    @unittest.skipIf(is_frozen, 'не повезло')
    def test_run(self):
        Run = Runner('Kate', 5)
        for i in range(10):
            Run.run()
        self.assertEqual(Run.distance, 100)

    @unittest.skipIf(is_frozen, 'не повезло')
    def test_challenge(self):
        Run1 = Runner('Vasya', 10)
        Run2 = Runner('Vera', 10)
        for i in range(10):
            Run1.walk()
            Run2.run()
        self.assertNotEqual(Run1.distance, Run2.distance)



if __name__ == '__main__':
    unittest.main()



