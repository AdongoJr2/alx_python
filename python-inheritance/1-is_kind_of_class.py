"""My module"""


def is_kind_of_class(obj, a_class):
    """Checks whether an object is an instance of,
    or if the object is an instance of a class that
    inherited from the specified class

    Args:
        obj (Any): The object to check
          a_class (Any): The class to check against
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
