# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Race, RaceDescription, RacePlayingFor
from .serializers import RaceSerializer, RaceDescriptionSerializer, RacePlayingForSerializer

# Create your views here.

class RacesView(APIView):
    def get(self, request):
        races = Race.objects.all()        
        serializer = RaceSerializer(races, many=True)
        return Response({"races": serializer.data})
