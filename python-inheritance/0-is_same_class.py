"""My module"""


def is_same_class(obj, a_class):
    """Checks whether the object is strictly an instance of
    the class passed

    Args:
        obj (Any): The object to check
        a_class (Any): The class to check against

    Returns:
        bool: The check result
    """
    if type(obj) == a_class:
        return True
    else:
        return False
