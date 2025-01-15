import runner_and_tournament as rt
import inspect
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.Runner1 = rt.Runner('Усейн', 10)
        self.Runner2 = rt.Runner('Андрей', 9)
        self.Runner3 = rt.Runner('Ник', 3)


    def Tournament_test(self):
        self.Tour = rt.Tournament(90, self.Runner1, self.Runner2, self.Runner3)
        TournamentTest.all_results = self.Tour.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())] == 'Ник')

    def test_test(self):
        self.Tournament_test()


    @classmethod
    def tearDownClass(cls):
        for item in cls.all_results.items():
            print(item)

if __name__ == '__main__':
    unittest.main()


