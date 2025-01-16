import logging
import unittest
import HumanMoveTest
import runner_test


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename = 'runner_test.log',
                        encoding='utf-8', format = "%(asctime)s||%(levelname)s||%(message)s")

    runtest = unittest.TestSuite()
    runtest.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(runtest)


