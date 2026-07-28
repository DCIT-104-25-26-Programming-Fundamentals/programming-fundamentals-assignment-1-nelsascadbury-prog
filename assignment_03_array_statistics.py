def calculate_statistics(numbers):
    if not numbers:
        return None, None, None, None
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum

if _name_ == "_main_":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in user_input.split()]
        
        if numbers:
            total, average, maximum, minimum = calculate_statistics(numbers)
            print(f"Sum: {total}")
            print(f"Average: {average}")
            print(f"Maximum: {maximum}")
            print(f"Minimum: {minimum}")
        else:
            print("No numbers were entered.")
    except ValueError:
        print("Please enter valid numbers.")
        print("Please enter valid numbers.")
