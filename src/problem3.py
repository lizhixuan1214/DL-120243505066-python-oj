def calculate_tax(p):
    tax = 0.0

    if p <= 1000:
        tax = 0
    elif p <= 3000:
        tax = p * 0.03
    elif p <= 5000:
        tax = p * 0.04
    else:
        tax = p * 0.06

    return tax

def process_output(result):
    # Check if the result is a whole number
    if result == int(result):
        return str(int(result))  # Return as integer string
    else:
        # Format to two decimal places, removing trailing zeros and decimal point if needed
        return f"{result:.2f}".rstrip('0').rstrip('.')

# Main execution with EOFError and input validation
try:
    pi = float(input())
    if pi < 0:
        raise ValueError("Input must be non-negative")
    k = calculate_tax(pi)
    print(process_output(k))  # Use process_output to format the result
except EOFError:
    exit(0)  # Exit gracefully on EOFError
except ValueError:
    exit(1)  # Exit with error code on invalid input
