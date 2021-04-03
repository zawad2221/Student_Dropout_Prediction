from django.shortcuts import render
from .models import StudentDetails
from .serializers import StudentDetailsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentDropoutPrediction(APIView):
    """
    List all students, or create a new student.
    """
    def get(self, request, format=None):
        student_details = StudentDetails.objects.all()
        serializer = StudentDetailsSerializer(student_details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data #Get all the request data/ form data

        #Do Prediction 

        data['result'] = 0 #Final result will set here

        serializer = StudentDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data['result'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)