from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import DayPlan
from .serializers import DayPlanSerializer

"""We need two views:
detail view for each day for each Child -> parent/teacher
list view for requested day for every Children ->teacher"""


class DayPlanDailyListView(generics.ListCreateAPIView):
    queryset = DayPlan.objects.all()
    serializer_class = DayPlanSerializer


class DayPlanDetailView(APIView):
    def get(self, request, pk, day):
        day_plan = DayPlan.objects.get(child_id=pk, day=day)
        serializer = DayPlanSerializer(day_plan)
        return Response(serializer.data)
