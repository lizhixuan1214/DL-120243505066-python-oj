def calculate_fee(hours):
    if hours <= 10:
        fee = 30
    elif 10 < hours <= 50:
        fee = hours * 3
    else:
        fee = hours * 2.5
    return fee

def process_output(result):
    # Check if the result is a whole number
    if result == int(result):
        return str(int(result))  # Return as integer string
    else:
        # Format to two decimal places, removing trailing zeros and decimal point if needed
        return f"{result:.2f}".rstrip('0').rstrip('.')

# Main execution with error handling
try:
    hours = float(input())
    if hours < 0:
        raise ValueError("Hours must be non-negative")
    fee = calculate_fee(hours)
    print(process_output(fee))
except EOFError:
    exit(0)  # Exit gracefully on EOFError
except ValueError:
    exit(1)  # Exit with error code on invalid input
