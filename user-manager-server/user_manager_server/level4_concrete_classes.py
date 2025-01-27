def __is_not_blank(self, string):
    """
    Checks if a given string is not empty or consists only of whitespace.

    Args:
      string: The string to be checked.

    Returns:
      True if the string is not empty and contains at least one non-whitespace character.
      False otherwise.
    """
    return string and string.strip()


def is_valid(self) -> bool:
    return self.__is_not_blank(self.username) & self.__is_not_blank(self.email)