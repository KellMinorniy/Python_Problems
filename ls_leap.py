def is_leap_year(year):
    if year %  4 !=  0:
        return False
    elif year %  100 !=  0:
        return True
    elif year %  400 !=  0:
        return False
    else:
        return True

year = int(input())
if  1900 <= year <=  10**5:
    print(is_leap_year(year))
else:
    print()