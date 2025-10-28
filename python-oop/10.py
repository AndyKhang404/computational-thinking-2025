class Logger:
	def log(self, message):
		print(f"[LOG]: {message}")

class FileWriter:
	def __init__(self, filename):
		self.filename = filename

	def write(self, text):
		with open(self.filename, 'a') as f:
			f.write(text + '\n')

class LogFileWriter(FileWriter, Logger):
	def __init__(self, filename):
		super().__init__(filename)

	def log(self, text):
		self.write(f"[LOG]: {text}")
	
log_writer = LogFileWriter("test.log")
log_writer.log("Application started")
log_writer.log("An error occurred")
log_writer.log("Application ended")