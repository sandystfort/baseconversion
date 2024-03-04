def decimal_to_base(decimal_number, base):
    if base < 2 or base > 16:
        return " Base is Invalid. enter a base between 2 and 16"
    
    if decimal_number < 0:
        return "Number is Invalid.  enter a non negative decimal number"
    
    digits = "0123456789ABCDEF"
    result = ""
    
    while decimal_number > 0:
        remainder = decimal_number % base
        result = digits[remainder] + result
        decimal_number = decimal_number // base
    
    return result or "0"

def main():
    try:
        decimal_number = int(input("Enter a non negative decimal number: "))
        base = int(input("Enter the base (between 2 and 16): "))
        
        if decimal_number < 0 or base < 2 or base > 16:
            print("Invalid input. make sure the decimal number is non-negative and the base is between 2 and 16")
        else:
            converted_value = decimal_to_base(decimal_number, base)
            print(f"The equivalent base-{base} value of decimal {decimal_number} is: {converted_value}")
    except ValueError:
        print("Input is invalid. enter integers only")

if __name__ == "__main__":
    main()
