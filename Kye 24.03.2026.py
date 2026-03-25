def parcel_code():
    while True:
        code = input("Input parcel code: ")
        
        if len(code) == 7 and code.isdigit():
            return code
        else:
            print("Please enter a 7-digit number")

def applying_pattern(code):
    first_six = code[:6]
    check_digit = int(code[6])

    digits = [int(d) for d in first_six]

    total = 0
    for i in range(6):
        total += digits[i] * (i + 1)

    calculated_digit = total % 10

    if calculated_digit == check_digit:
        return True, "Valid parcel code."
    else:
        return False, "Invalid parcel code."

def main():
    code = parcel_code()
    result, message = applying_pattern(code)
    print(message)

main()