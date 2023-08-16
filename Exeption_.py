

class TriangError(Exception):

    def __str__(self):
        return f"таких сторон в треугольнике не бывает"




def triangrle(a, b, c):
    if not (a <= b + c) or not (b <= a + c) or not (c <= b + a):
        raise TriangError

    tr = "Равнобедренный треугольник"
    if a == b == c:
        tr = "Равносторонний треугольник"
    elif a != b and b!= c and a!= c:
        tr = "Разносторонний треугольник"
    return tr

try:
    print(triangrle(1, 6, 8))
except TriangError as e:
    print(e)
