from celery import Celery

from exceptions import ImportError, Exception
from www import settings


app = Celery('tasks', broker=settings.BROKER, backend=settings.CELERY_RESULT_BACKEND)

class VeggyMonitor():
	def __init__(self, *args, **kwargs):
		""" 
		the veggy monitor class implements celery event handlers for 
		worker-heartbeat
		"""
		self.state = app.events.State()
		self.data = {}

		def get_worker_heartbeat(event):
			gen = (val for val in self.state.event(event) if val is not None)
			for val in gen:
				print val
				
			print "STATE_EVENT: %s\nEVENT %s" % (self.state.event(event), event)
		
		with app.connection() as connection:
			recv = app.events.Receiver(connection, handlers={
				'worker-heartbeat': get_worker_heartbeat,
	#			'task-sent': get_task_sent,
			})
			recv.capture(limit=None, timeout=None, wakeup=True)


class VeggyTaskHandler():
	def __init__(self, *args, **kwargs):
		pass

	@app.task
	def add(x, y):
		print x, y
		total = x + y
		print 'total: ', total
		return total
