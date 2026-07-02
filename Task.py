import datetime
import csv

class Task:
    def __init__(self, taskName: str, completeStatus = "Incomplete", date = datetime.datetime.now().strftime("%x")):
        self.name = taskName
        self.completeStatus = completeStatus
        self.date = date

    def __str__(self) -> str:
        return f"Task Name: {self.name} | Completedness: {self.completeStatus} | Date: {self.date}"

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self):
        return self.name

    def markIncomplete(self) -> None:
        self.setStatus("Incomplete")

    def markComplete(self) -> None:
        self.setStatus("Complete")

    def getStatus(self):
        return self.completeStatus

    def setDate(self, date: datetime) -> None:
        self.date = date

    def getDate(self) -> datetime:
        return self.date

    def taskObjToCSVInfo(self):
        return [self.name, self.completeStatus, self.date]

    @staticmethod
    def saveTasksToFile(taskList: list) -> None:
        taskListFile = open("taskList.txt", "w")
        writer = csv.writer(taskListFile, delimiter=",")
        for task in taskList:
            writer.writerow(task.taskObjToCSVInfo())
        taskListFile.close()

    @staticmethod
    def readTasksFromFile() -> list:
        taskObjList = []
        try:
            taskListFile = open("taskList.txt", "rt")
        except FileExistsError:
            return "File Doesn't Exist"
        else:
            reader = csv.reader(taskListFile, delimiter=",")
            taskListCSVFormat = [row for row in reader]
        for taskCSVInfo in taskListCSVFormat:
            taskObjList.append(Task(taskCSVInfo[0], taskCSVInfo[1], datetime.datetime.strptime(taskCSVInfo[2], "%m/%d/%y").date()))
        taskListFile.close()
        return taskObjList

