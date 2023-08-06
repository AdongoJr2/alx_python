"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the __str__ method

        Returns:
            str: [Square] (`id`) `x`/`y` - `size`
        """
        return "[Square] ({id}) {x}/{y} - {size}".format(
            id=self.id,
            x=self.x, y=self.y,
            size=self.width
        )
