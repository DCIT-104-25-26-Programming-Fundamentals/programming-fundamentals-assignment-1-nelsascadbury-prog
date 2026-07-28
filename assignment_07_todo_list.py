def todo_list_app():
    tasks = []
    while True:
        print("\n--- To-Do List App ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nTasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "2":
            task = input("Enter the task to add: ")
            tasks.append(task)
            print(f"'{task}' has been added.")
        elif choice == "3":
            if not tasks:
              print("Your to-do list is empty.")
            else:
              try:
                 task_num =
                int(input("Enter the task number to remove:"))
                  if 1 <= task_num <= len(tasks):
                  removed = tasks.pop(task_num-1)
                            print(f"'{removed}' has been removed.")
                  else:
                    print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid integer.")
        elif choice == "4":
            print("Exiting To-Do List App.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    todo_list_app()
                                                       
             …
