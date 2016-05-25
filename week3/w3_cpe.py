idef ndigits(x):
    '''
    This function takes an integer ‘x’ (either positive or negative)
    as an argument and returns the number of digits in the integer x.
    x - integer (positive or negative)
    result - integer (number of digits in x)
    '''
    # Remove minus sign
    absX = abs(x)

    if x == 0:
        # 0 - case
        return 0
    elif absX < 10:
        # Base case
        return 1
    else:
        # Recursion case
        return 1 + ndigits(absX / 10)
