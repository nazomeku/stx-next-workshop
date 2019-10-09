import calendar


def leap_year(year: int) -> bool:
    """Check if provided year is a leap year.

    Args:
        year (int): Parameter to check against isleap function.

    Returns:
        bool: True if leap year, False otherwise.

    Raises:
        TypeError: If `year` parameter is not an integer.

    """
    if not isinstance(year, int):
        raise TypeError('Please provide proper year value')
    return calendar.isleap(year)
