def calculate_bonus(p):
    bonus = 0.0

    if p <= 10:
        bonus = p * 0.1
    elif p <= 20:
        bonus = 10 * 0.1 + (p - 10) * 0.075
    elif p <= 40:
        bonus = 10 * 0.1 + 10 * 0.075 + (p - 20) * 0.05
    elif p <= 60:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (p - 40) * 0.03
    elif p <= 100:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (p - 60) * 0.015
    else:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (p - 100) * 0.01

    return bonus

def process_output(result):
    # Check if the result is a whole number
    if result == int(result):
        return str(int(result))  # Return as integer string
    else:
        # Convert to string and remove trailing zeros and unnecessary decimal point
        return str(float(result)).rstrip('0').rstrip('.')

# Main execution with EOFError handling
try:
    pi = float(input())
    k = calculate_bonus(pi)
    print(process_output(k))  # Use process_output to format the result
except EOFError:
    exit(0)  # Exit gracefully on EOFError
except ValueError:
    exit(1)  # Exit with error code on invalid input
