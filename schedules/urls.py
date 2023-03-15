from django.urls import path

from .views import DayPlanDailyListView, DayPlanDetailView

""" list view of all children instances for current day
detail view for child for curreny day
archive page for passed days """

urlpatterns = [
    # list view for all children on current day
    path("", DayPlanDailyListView.as_view(), name="daily_list"),
    # detail view for each child on requested date
    path("child/<int:pk>/<str:day>/", DayPlanDetailView.as_view(), name="daily_detail"),
]
