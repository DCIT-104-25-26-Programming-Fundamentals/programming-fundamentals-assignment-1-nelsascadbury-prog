def multiplication_table(n):
    return [[i * j for j in range(1, 11)] for i in range(1, n + 1)]

if __name__ == "__main__":
    try:
        n = int(input("Enter the number up to which you want the multiplication table: "))
        table = multiplication_table(n)
        for row in table:
            print(row)
    except ValueError:
        print("Please enter a valid integer.")
