"""
This is how I teach special (magic) methods.
"""


class Point:
    color = "red"

    def __init__(self, x, y):  # initialize
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)


if __name__ == "__main__":
    point_1 = Point(2, 3)
    point_2 = Point(0, 0)
    point_3 = Point.zero()
    print(point_1)
    print(point_2 == point_3)
    print(point_1 == point_2)
    print(point_1 + point_1)
    print(point_1 * 10)




