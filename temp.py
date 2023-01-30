def is_year_leap(year):
    if year != 1900:
        if year % 4 == 0:
            return True
        else:
            return False
    else:
        return False

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print(1)
        return 31
    elif month in [4, 6, 9, 11]:
        print(2)
        return 30
        
    else:
        if is_year_leap(year)== True:
            print(3)
            return 29
        else:
            print(4)
            return 28
def day_of_year(year, month, day):
    result = day
    for i in range(1, month):
        result += days_in_month(year, i)
    return result

print(day_of_year(2000, 6, 24))