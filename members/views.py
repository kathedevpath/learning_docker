from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .permissions import (
    ParentOnlyViewAndTeacherEdit,
    OnlyStaffCanSeeListViews,
)
from .models import Child, Parent
from .serializers import ChildSerializer, ParentSerializer


class ChildList(generics.ListCreateAPIView):
    permission_classes = [OnlyStaffCanSeeListViews]
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ChildDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [ParentOnlyViewAndTeacherEdit]
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ParentList(generics.ListCreateAPIView):
    permission_classes = [OnlyStaffCanSeeListViews]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
