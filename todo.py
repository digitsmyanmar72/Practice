# todo.py

# Initialize an empty list to store tasks
tasks = []

# Function to display menu options
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Exit")

# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to remove a task
def remove_task():
    view_tasks()
    if len(tasks) > 0:
        task_num = int(input("Enter the number of the task to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")

# Main function to run the to-do list app
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the to-do list app. Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.")

# Run the main function
if __name__ == "__main__":
    main()
