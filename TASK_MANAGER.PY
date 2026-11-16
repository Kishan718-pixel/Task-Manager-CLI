tasks = []


def add_task():
    print("\n----- ADD NEW TASK -----")

    task_name = input("Enter task name: ").strip()

    
    if task_name == "":
        print("Error: Task name cannot be empty!")
        return

    task = {
        "id": len(tasks) + 1,
        "name": task_name,
        "status": "Pending"
    }

    tasks.append(task)

    print("Task added successfully!")



def view_tasks():
    print("\n----- ALL TASKS -----")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for task in tasks:
        print("\nTask ID:", task["id"])
        print("Task Name:", task["name"])
        print("Status:", task["status"])



def complete_task():
    print("\n----- COMPLETE TASK -----")

    if len(tasks) == 0:
        print("No tasks available to complete.")
        return

    try:
        task_id = int(input("Enter Task ID: "))

        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "Completed":
                    print("Task is already completed!")
                else:
                    task["status"] = "Completed"
                    print("Task marked as completed!")
                return

        print("Invalid Task ID!")

    except ValueError:
        print("Please enter a valid numeric ID!")



def delete_task():
    print("\n----- DELETE TASK -----")

    if len(tasks) == 0:
        print("No tasks available to delete.")
        return

    try:
        task_id = int(input("Enter Task ID: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task deleted successfully!")
                return

        print("Invalid Task ID!")

    except ValueError:
        print("Please enter a valid numeric ID!")



def main():

    while True:

        print("\n==============================")
        print("       TASK MANAGER")
        print("==============================")

        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        print("==============================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("\nThank you for using Task Manager!")
            print("Application closed successfully.")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()