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
        """Checks whether the value passed is an integer

        Args:
            value (Any): The value to check
            attribute_name (str, optional): The property name. Defaults to "".

        Raises:
            TypeError: Raised when the `value` is not an integer
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute_name))

    def __gt_0_check(self, value, attribute_name=""):
        """Check to ensure that the value passed is greater than zero (0)

        Args:
            value (Any): The value to check
            attribute_name (str, optional): The property name. Defaults to "".

        Raises:
            ValueError: Raised when `value` is less than zero (0)
        """
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute_name))

    def __gte_0_check(self, value, attribute_name=""):
        """Check to ensure that the value passed is greater than or equal to zero (0)

        Args:
            value (Any): The value to check
            attribute_name (str, optional): The property name. Defaults to "".

        Raises:
            ValueError: Raised when `value` is less than or equal to zero (0)
        """

        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute_name))

    def area(self):
        """Returns the area value of the Rectangle instance

        Returns:
            int: The area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""

        for _ in range(self.height):
            for _ in range(self.width):
                print("#", end="")

            print()

    def __str__(self):
        """Overrides the __str__ method

        Returns:
            str: [Rectangle] (`id`) `x`/`y` - `width`/`height`
        """
        res = "[Rectangle] ({id}) {x}/{y} - {width}/{height}".format(
            id=self.id, x=self.x, y=self.y, width=self.width, height=self.height
        )

        return res
