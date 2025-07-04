def main():
    tasks = []
    completed = []

    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark task as completed")
        print("5. View completed tasks")
        print("6. Clear all tasks")
        print("7. Show number of tasks")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            tasks.append(task_name)
            print(f"Task '{task_name}' added.")

        elif choice == '2':
            if tasks:
                print("\nPending Tasks:")
                for i in range(1, len(tasks) + 1):
                    print(f"{i}. {tasks[i - 1]}")
            else:
                print("No pending tasks.")

        elif choice == '3':
            if tasks:
                try:
                    task_index = int(input("Enter the task number to remove: ")) - 1
                    if 0 <= task_index < len(tasks):
                        removed_task = tasks.pop(task_index)
                        print(f"Task '{removed_task}' removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to remove.")

        elif choice == '4':
            if tasks:
                try:
                    task_index = int(input("Enter the task number to mark as completed: ")) - 1
                    if 0 <= task_index < len(tasks):
                        completed_task = tasks.pop(task_index)
                        completed.append(completed_task)
                        print(f"Task '{completed_task}' marked as completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to complete.")

        elif choice == '5':
            if completed:
                print("\nCompleted Tasks:")
                for i in range(1, len(completed) + 1):
                    print(f"{i}. {completed[i - 1]}")
            else:
                print("No completed tasks.")

        elif choice == '6':
            tasks.clear()
            completed.clear()
            print("All tasks cleared.")

        elif choice == '7':
            print(f"Pending tasks: {len(tasks)}")
            print(f"Completed tasks: {len(completed)}")

        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
