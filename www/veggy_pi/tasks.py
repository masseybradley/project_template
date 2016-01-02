from celery import Celery

from exceptions import ImportError, Exception
from www import settings


app = Celery('tasks', broker='amqp://guest@localhost/', backend=settings.CELERY_RESULT_BACKEND)

class VeggyTaskHandler():
	def __init__(self, *args, **kwargs):
		self.x = 0
		self.y = 0

	@app.task
	def add(self):
		print self.x, self.y
		total = self.x + self.y
		print "total: ", total
		return total
