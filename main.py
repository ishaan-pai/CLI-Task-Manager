import Task
import datetime

while (1):
    taskList = Task.Task.readTasksFromFile()

    print("\n")
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
                print("Further Options: Add Task, Update Task, Delete Task, Mark Tasks, Return to Main Menu")
                viewMenuChoice = input("Choice: ")

                match viewMenuChoice:
                    case "Add":
                        taskName = input("What are we calling the task?: ")
                        taskList.append(Task.Task(taskName))
                        Task.Task.saveTasksToFile(taskList)
                        print("Task Added! \n")
                    case "Update":
                        updateScore = 0
                        taskName = input("What task would you like to update?: ")
                        for task in taskList:
                            if task.getName() == taskName:
                                print("How would you like to update the task? Update Name, Update Date")
                                updateMenuChoice = input("Your Choice: ")
                                match updateMenuChoice:
                                    case "Name":
                                        updatedName = input("What would you like the new name to be?: ")
                                        task.setName(updatedName)
                                    case "Date":
                                        updatedDate = input("What would you like the new date to be? (mm/dd/yy): ")
                                        task.setDate(datetime.datetime.strptime(updatedDate, "%m/%d/%y").date())
                        Task.Task.saveTasksToFile(taskList)
                    case "Delete":
                        deletionScore = 0
                        taskName = input("What task would you like to delete?: ")
                        for task in taskList:
                            if task.getName() == taskName:
                                taskList.remove(task)
                                print("Task Deleted !")
                                Task.Task.clearFile()
                                deletionScore += 1
                                break
                        if deletionScore == 0:
                            print("Task does not exist to delete.")
                        Task.Task.saveTasksToFile(taskList)
                    case "Mark":
                        markScore = 0
                        taskName = input("What task would you like to mark?: ")
                        for task in taskList:
                            if task.getName() == taskName:
                                wantedCompletionStatus = input("Mark as Complete or Incomplete?: ")
                                match wantedCompletionStatus:
                                    case "Complete":
                                        task.markComplete()
                                        markScore += 1
                                    case "Incomplete":
                                        task.markIncomplete()
                                        markScore += 1
                        if markScore == 0:
                            print("Task does not exist to mark.")
                        Task.Task.saveTasksToFile(taskList)
                    case "Return":
                        break

        case "Exit":
            Task.Task.saveTasksToFile(taskList)
            break
        case _:
            print("That is not an option\n")

