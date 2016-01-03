from veggy_pi.models import *

from rest_framework import serializers


class RPiPinSerializer(serializers.ModelSerializer):
	class Meta:
		model = RPiPin
