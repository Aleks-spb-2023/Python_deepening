import unittest

def triangrle(a, b, c):
    if not (a <= b + c) or not (b <= a + c) or not (c <= b + a):
        raise TypeError("Треугольник не существует")

    tr = "Равнобедренный треугольник"
    if a == b == c:
        tr = "Равносторонний треугольник"
    elif a != b and b!= c and a!= c:
        tr = "Разносторонний треугольник"
    return tr


class TestTriangle(unittest.TestCase):

    def test_rav(self):
        self.assertEqual(triangrle(5, 5, 5), "Равносторонний треугольник")

    def test_bedr(self):
        self.assertEqual(triangrle(2, 2, 3), "Равнобедренный треугольник")

unittest.main(verbosity=2)