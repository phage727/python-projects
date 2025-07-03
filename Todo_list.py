def main():
    task = []

    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            task_name = input("Enter the task name: ")
            task.append(task_name)
            print(f"Task '{task_name}' added.")

        elif choice == '2':
            if task:
                print("Tasks:")
                for i in range(1, len(task) + 1):
                    print(f"{i}. {task[i - 1]}")

            else:
                print("No tasks available.")

        elif choice == '3':
            if task:
                task_index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_index < len(task):
                    removed_task = task.pop(task_index)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks available to remove.")

        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()