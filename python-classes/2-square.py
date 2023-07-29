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

    def area(self):
        return self.__size * self.__size
