def date(day,month,year):
    if day < 1:
        return False
    if month < 1 or month > 12:
        return False
    months_31 = [1,3,5,7,8,10,12]
    months_30 = [4,6,9,11]
    if month in months_31:
        if day > 31:
            return False
    elif month in months_30:
        if day > 30:
            return False
    elif month == 2:
        if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    else:
        return True
 

