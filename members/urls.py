from django.urls import path

from .views import ChildList, ChildDetail, ParentList, ParentDetail

urlpatterns = [
    path("children/", ChildList.as_view(), name="children_list"),
    path("child/<int:pk>/", ChildDetail.as_view(), name="child_detail"),
    path("parent/", ParentList.as_view(), name="parent_list"),
    path("parent/<int:pk>", ParentDetail.as_view(), name="parent_detail"),
]
