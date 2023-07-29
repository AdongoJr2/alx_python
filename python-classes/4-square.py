"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the data

        Args:
            size (int, optional): Size of one side of the suare. Defaults to 0.

        Raises:
            TypeError: raised when ``size`` is not an integer
            ValueError: raised when ``size`` is less than zero (0)
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """A getter for the privte instance attribute `__size`

        Returns:
            int: The value of size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the __size value

        Args:
            value (int): The value to assign to `__self`

        Raises:
            TypeError: raised when ``size`` is not an integer
            ValueError: raised when ``size`` is less than zero (0)
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates the area of the square

        Returns:
            int: The area of the square
        """

        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return

        for _ in range(self.size):
            for _ in range(self.size):
                print("#", end="")

            print()
