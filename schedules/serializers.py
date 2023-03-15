from rest_framework import serializers

from .models import DayPlan


class DayPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayPlan
        fields = "__all__"
