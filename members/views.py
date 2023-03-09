from django.http import Http404
from rest_framework import generics
from .permissions import IsParent
from .models import Child, Parent
from .serializers import ChildSerializer, ParentSerializer


class ChildList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ChildDetail(generics.RetrieveAPIView):
    serializer_class = ChildSerializer

    def get_object(self):
        child_id = self.kwargs["pk"]

        try:
            child = Child.objects.get(id=child_id)
            self.check_object_permissions(self.request.user, child.parent)
            return child
        except Child.DoesNotExist:
            raise Http404


class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
