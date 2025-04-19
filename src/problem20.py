def calculate_fee(weight):
    if weight <= 50:
        fee = weight * 0.15
    else:
        fee = 50 * 0.15 + (weight - 50) * 0.25
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
    weight = float(input())
    if weight < 0:
        raise ValueError("weight must be non-negative")
    fee = calculate_fee(weight)
    print(process_output(fee))
except EOFError:
    exit(0)  # Exit gracefully on EOFError
except ValueError:
    exit(1)  # Exit with error code on inv
