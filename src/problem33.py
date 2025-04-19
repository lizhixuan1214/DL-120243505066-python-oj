def calculate_tax(income):
    if income <= 1000:  
        tax = 0
    elif income <= 3000:  
        tax = income * 0.03
    elif income <= 5000:  
        tax = income * 0.04
    else: 
        tax = income * 0.06
    return int(tax)  


input_data = input().split() 
n = int(input_data[0]) 
incomes = list(map(int, input_data[1:])) 

taxes = [calculate_tax(income) for income in incomes]

print(" ".join(map(str, taxes)))
