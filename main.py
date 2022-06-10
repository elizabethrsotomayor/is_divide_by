def is_divide_by(number: int, a: int, b: int) -> bool:
    """
    Check if an integer is divisible by both integers a and b
    :param number: the integer to check to see if it is evenly divisible
    :param a:
    :param b:
    :return:
    """
    return number % a == 0 and number % b == 0
