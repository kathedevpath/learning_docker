from django.urls import path

from .views import DayPlanDailyListView, DayPlanDetailView

""" list view of all children instances for current day
detail view for child for curreny day
archive page for passed days """

urlpatterns = [
    path("", DayPlanDailyListView.as_view(), name="daily_list"),
]
