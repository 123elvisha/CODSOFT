
def task():
    task_list = []
    print("Welcome to the task management app")

    total_task = int(input("Enter how many tasks you want to add: "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        task_list.append(task_name)

        print(f"Today's tasks are:\n{task_list}")

    while True:
        operation = int(input("Enter:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        if operation == 1:
            add_task = input("Enter task you want to add: ")
            task_list.append(add_task)
            print(f"Task '{add_task}' has been successfully added...")

        elif operation == 2:
            update_task = input("Enter the task name you want to update: ")
            if update_task in task_list:
                new_task = input("Enter new task: ")
                index = task_list.index(update_task)
                task_list[index] = new_task
                print(f"Updated task '{update_task}' to '{new_task}'")
            else:
                print(f"Task '{update_task}' not found.")

        elif operation == 3:
            delete_task = input("Which task you want to delete: ")
            if delete_task in task_list:
                index = task_list.index(delete_task)
                del task_list[index]
                print(f"Task '{delete_task}' has been deleted...")
            else:
                print(f"Task '{delete_task}' not found.")

        elif operation == 4:
            print(f"Total tasks: {len(task_list)}")
            print(f"Task list: {task_list}")

        elif operation == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid input")

    print("Goodbye!")

task()