from enum import Enum

class TaskStatus(Enum):
	PENDING = "pending"
	DONE = "done"

class PriorityLevel(Enum):
	LOW = ("Low",1)
	MEDIUM = ("Medium",2)
	HIGH = ("High",3)

class Task:
	def __init__(self, description, priority):
		self.description = description
		self.priority = priority
		self.status = TaskStatus.PENDING

class TaskManager:
	def __init__(self):
		self.tasks = []

	def add_task(self, task=None):
		if task is not None:
			self.tasks.append(task)
			return
		description = input("Enter task description: ")
		priority_inp = input("Enter task priority (low, medium, high): ")
		priority = PriorityLevel.LOW
		match priority_inp.lower().strip():
			case "low":
				priority = PriorityLevel.LOW
			case "medium":
				priority = PriorityLevel.MEDIUM
			case "high":
				priority = PriorityLevel.HIGH
			case _:
				print("Invalid priority, setting to Low by default.")
		task = Task(description, priority)
		self.tasks.append(task)
		self.tasks.sort(key=lambda t: (t.status == TaskStatus.DONE, -t.priority.value[1]))

	def mark_completed(self, description):
		for task in self.tasks:
			if task.description != description: continue
			task.status = TaskStatus.DONE
			self.tasks.sort(key=lambda t: (t.status == TaskStatus.DONE, -t.priority.value[1]))
			return True
		return False

	def change_priority(self, description, new_priority):
		for task in self.tasks:
			if task.description != description: continue
			task.priority = new_priority
			self.tasks.sort(key=lambda t: (t.status == TaskStatus.DONE, -t.priority.value[1]))
			return True
		return False

	def list_tasks(self):
		print("Tasks:")
		for task in self.tasks:
			print(f"[{'*' if task.status == TaskStatus.DONE else ' '}][{task.priority.value[0]}] {task.description}")

task_manager = TaskManager()
task_manager.add_task(Task("Finish homework", PriorityLevel.HIGH))
task_manager.add_task(Task("Learning Python", PriorityLevel.HIGH))
task_manager.add_task(Task("Doing laundry", PriorityLevel.MEDIUM))
task_manager.list_tasks()
print()
task_manager.mark_completed("Finish homework")
task_manager.list_tasks()
print()
task_manager.change_priority("Learning Python", PriorityLevel.LOW)
task_manager.list_tasks()
print()