def student_records_app():
    records = {}
    while True:
        print("\n--- Student Records App ---")
        print("1. Add/Update Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            name = input("Enter student name: ").strip()
            if name:
                try:
                    score = float(input("Enter student score: "))
                    records[name] = score
                    print(f"Record for '{name}' has been saved.")
                except ValueError:
                    print("Please enter a valid numeric score.")
            else:
                print("Name cannot be empty.")
        elif choice == "2":
            name = input("Enter student name to search: ").strip()
            if name in records:
                print(f"Student: {name} | Score: {records[name]}")
            else:
                print("Student not found.")
        elif choice == "3":
            if not records:
                print("No student records found.")
            else:
                print("\nAll Student Records:")
                for name, score in records.items():
                    print(f"- {name}: {score}")
        elif choice == "4":
            print("Exiting Student Records App.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
  student_records_app()
  
    student_records_app()
