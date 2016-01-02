from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


from www import settings


class RPiPinMap(models.Model):
	label = models.CharField(max_length=50, blank=False, null=False)
	pin_number = models.SmallIntegerField(blank=False, null=False)
	is_gpio = models.BooleanField()
	def __unicode__(self):
		return "label: %s pin: %s" % (self.label, self.pin_number)

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
		# interval = on period + off period
		# on_period = start + on
		# off_period = on_period + off
		interval = self.on + self.off 
		# total duration = end - start
		duration = self.end - self.start
		# total repeat timers = duration / intervals 
		timers = duration.total_seconds() / interval.total_seconds()
		print "interval: %s\nduration: %s\non: %s\noff: %s\ntimers: %s" % (interval, duration, self.on, self.off, timers)
		
# Create your models here.
