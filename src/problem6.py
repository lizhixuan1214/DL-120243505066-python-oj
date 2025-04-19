def calculate_wage(hours):
    if hours <= 0:
        return 0  
    elif hours <= 4:
        wage = 50  
    elif hours <= 8:
        wage = 50 + (hours - 4) * 20  
    else:
        wage = 50 + 4 * 20 + (hours - 8) * 30  
    return wage

hours = int(input())
print(calculate_wage(hours))
