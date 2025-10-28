class Robot:
	active_robots = 0

	def __init__(self, name):
		self.name = name
		Robot.active_robots += 1
	
	@classmethod
	def number_active(cls):
		return cls.active_robots
	
	def remove(self):
		Robot.active_robots -= 1

robots = [Robot("robot1"), Robot("robot2"), Robot("robot3")]
print("Active robots:", Robot.number_active())
robots[0].remove()
print("Active robots:", Robot.number_active())