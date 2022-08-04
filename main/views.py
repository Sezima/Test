from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter

from .models import *
from .serializers import TeacherSerializer, StudentsSerializer, SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class Search(generics.ListAPIView):
    """Поиск"""
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class SchoolListView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


