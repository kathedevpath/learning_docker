from rest_framework import generics

from .models import DayPlan
from .serializers import DayPlanSerializer


class DayPlanDailyListView(generics.ListCreateAPIView):
    queryset = DayPlan.objects.all()
    serializer_class = DayPlanSerializer


class DayPlanDetailView(generics.RetrieveUpdateAPIView):
    queryset = DayPlan.objects.all()
    serializer_class = DayPlanSerializer
