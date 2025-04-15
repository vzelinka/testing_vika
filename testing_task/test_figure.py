import unittest
from random import choice, randint
from app import Figure

class TestFigure(unittest.TestCase):

    def setUp(self) -> None:
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)

    def tearDown(self) -> None:
        del self.obj

    def test_figure_type(self):
        self.assertEqual(self.figure, self.obj.get_figure_type, "Невірний тип фігури!")

    def test_figure_length(self):
        self.assertEqual(self.length, self.obj.get_figure_length, "Невірна довжина фігури!")

    def test_invalid_figure_type(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 5)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", -3)

if __name__ == '__main__':
    unittest.main()
