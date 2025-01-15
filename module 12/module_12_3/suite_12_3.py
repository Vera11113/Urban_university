import unittest
import module_12_1
import module_12_2

test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity = 2)
runner.run(test)
