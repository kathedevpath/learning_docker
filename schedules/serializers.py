from rest_framework import serializers

from .models import DayPlan


class DayPlanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "day",
            "child",
            "meals_at_school",
            "behaviour",
            "summary",
        )
        model = DayPlan
