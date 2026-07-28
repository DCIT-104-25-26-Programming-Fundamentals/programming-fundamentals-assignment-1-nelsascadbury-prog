def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms: "))
        result = fibonacci_sequence(n)
        print(f"Fibonacci sequence: {result}")
    except ValueError:
        print("Please enter a valid integer.")
