"""Rectangle module"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def print(self):
        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
