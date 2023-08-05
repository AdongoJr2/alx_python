"""The Rectangle moduke"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if id is not None:
            self.__integer_check(id, "id")

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__integer_check(value, "width")
        self.__gt_0_check(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__integer_check(value, "height")
        self.__gt_0_check(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__integer_check(value, "x")
        self.__gte_0_check(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__integer_check(value, "y")
        self.__gte_0_check(value, "y")
        self.__y = value

    def __integer_check(self, value, attribute_name=""):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute_name))

    def __gt_0_check(self, value, attribute_name=""):
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute_name))

    def __gte_0_check(self, value, attribute_name=""):
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute_name))
