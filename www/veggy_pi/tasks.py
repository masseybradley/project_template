from celery import Celery

from exceptions import ImportError, Exception

app = Celery('tasks', broker='amqp://guest@localhost//')

class VeggyTaskHandler():
	def __init__(self, *args, **kwargs):
		self.x = 0
		self.y = 0

	@app.task
	def add(self):
		print self.x, self.y
