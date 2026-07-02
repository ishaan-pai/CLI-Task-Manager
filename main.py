import Task

while (1):
    taskList = Task.Task.readTasksFromFile()

    print("What would you like to do?\n")
    print("- View all tasks")
    print("- Save and Exit")
    print("\n")

    mainMenuChoice = input("Choice: ")
    print("\n")

    match mainMenuChoice:
        case "View":
            while(1):
                if len(taskList) == 0:
                    print("No tasks available...")
                else:
                    print("All Tasks: ")
                    for task in taskList:
                        print("- " + str(task) + "\n")
                print("Further Options: Add Task, Update Task, Delete Task, Return to Main Menu")
                viewMenuChoice = input("Choice: ")

                match viewMenuChoice:
                    case "Add":
                        taskName = input("What are we calling the task?: ")
                        taskList.append(Task.Task(taskName))
                        Task.Task.saveTasksToFile(taskList)
                        print("Task Added! \n")
                    case "Update":
                        pass
                    case "Delete":
                        taskName = input("Which task would you like to delete?: ")
                        for task in taskList:
                            if task.getName() == taskName:
                                taskList.remove(task)
                            else:
                                print("Task doesn't exist to delete.")
                    case "Return":
                        break

        case "Exit":
            Task.Task.saveTasksToFile(taskList)
            break
        case _:
            print("That is not an option\n")

