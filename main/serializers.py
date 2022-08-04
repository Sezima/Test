from rest_framework import serializers
from .models import *


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teach
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
