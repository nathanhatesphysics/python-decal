def fact_loop(num):
    """
    >>> fact_loop(7)
    5040
    """
    total = 1
    for i in range(num, 0, -1):
        total *= i
    return total
print(fact_loop(4))

if __name__ == "__main__":
    import doctest
    doctest.testmod()