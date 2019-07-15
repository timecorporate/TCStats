# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from stats.serializers import UserSerializer
from stats.models import User

# Create your views here.


class UserView(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
