def calculate_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B+'
    elif score >= 65:
        return 'B'
    elif score >= 60:
        return 'C+'
    elif score >= 55:
        return 'C'
    elif score >= 50:
        return 'D+'
    elif score >= 45:
        return 'D'
    else:
        return 'E/F'

if _name_ == "_main_":
    try:
        score = float(input("Enter student score (0-100): "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"The grade is: {grade}")
        else:
            print("Score must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")
        print("Please enter a valid number.")
