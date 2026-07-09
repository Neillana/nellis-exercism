def leap_year(year):
    """Return True if `year` is a leap year according to the Gregorian calendar rules.
    
    A year is a leap year if:
    - it is divisible by 400, or
    - it is divisible by 4 but not by 100.
    """
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
