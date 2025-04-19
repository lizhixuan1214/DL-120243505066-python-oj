def isleapyear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dayofyear(year, month, day):

    daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if isleapyear(year):
        daysinmonth[1] = 29
    
    days = sum(daysinmonth[:month - 1]) + day
    
    return days

year, month, day = map(int, input().split())

print(dayofyear(year, month, day))
