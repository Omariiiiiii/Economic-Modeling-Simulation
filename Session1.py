# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# a = Point(2, 3)
# b = Point(7, 9)
#
# print(f"a={a.x}, {a.y})")
# print(f"b={a.x}, {a.y})")
#
# import random
#
# # class Point:
# #     def __init__(self, x=None, y=None):
# #         self.x = random.randint(1, 10) if x is None else x
# #         self.y = random.randint(1, 10) if y is None else y
# #
# # # Creating a list of 5 random points
# # points = [Point() for _ in range(5)]
# #
# # for i, point in enumerate(points):
# #     print(f"Point {i+1}=({point.x}, {point.y})")
#
# points = []
# for _ in range(5):
#     x = random.randint(-100, 100)
#     y = random.randint(-100, 100)
#     random_point = Point(x, y)
#     points.append(random_point)
#
#     points.append(Point(random.randint(-100, 100),
#                         random.randint(-100, 100)))
#
#
# for point in points:
#     print(f"n{point.x}, {point.y})")


class Point:
    def __init__(self, x, y):
        """

        :param x:
        :param y:
        """
        self.x = x
        self.y = y
    def __str__(self):
        """

        :return:
        """
        return f"p({self.x}, {self.y})"
