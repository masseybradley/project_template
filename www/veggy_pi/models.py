from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class GenericGPIO(models.Model):
	pin_number = models.IntegerField(null=False)
	class Meta:
		abstract = True

class GPIO(GenericGPIO):
	is_three = models.NullBooleanField()
	is_five = models.NullBooleanField()

class TimerConfiguration(models.Model):
	time_duration = models.DurationField(null=False, blank=False)
	def __unicode__(self):
		return self.time_duration
#	def set_time_duration(self, start, end):


class TemperatureConfiguration(models.Model):
	max_temperature = models.IntegerField(null=False, default=0)
	min_temperature = models.IntegerField(null=False, default=0)
	def __unicode__(self):
		return "min: %s max: %s" % (self.max_temperature, self.min_temperature)

# Create your models here.
