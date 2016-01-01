from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class GenericTimer(models.Model):
	"""
	generic timer class to be sublclassed by timer implementations
	"""
	start = models.DateTimeField(blank=False, null=False)
	end = models.DateTimeField(blank=False, null=False)
	def clean(self):
		if self.end < self.start:
			raise ValidationError(_('end time can not be inferieur to start time.'))
	class Meta:
		abstract = True

class RepeatTimer(GenericTimer):
	"""
	repeat timer for elements that need to switch on for a timed duration
	over a defined period of time.
	"""
	on = models.DurationField(blank=False, null=False)
	off = models.DurationField(blank=False, null=False)
	def __unicode__(self):
		return "on: %s - off: %s (between: %s and %s)" % (self.on, self.off, self.start, self.end)
	def generate_timer(self):
		# total of timer duration = on period + off period
		interval = self.on + self.off
		duration = self.end - self.start
		timers = duration.total_seconds() / interval.total_seconds()
		print "interval: %s\nduration: %s\non: %s\noff: %s\ntimers: %s" % (interval, duration, self.on, self.off, timers)
		return duration, interval
		

	# def repeat_timer(self, hours, duration):

# Create your models here.
