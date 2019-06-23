# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
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
from .serializers import RaceSerializer, RaceDescriptionSerializer, RacePlayingForSerializer, RaceListSerializer

# Create your views here.

class RacesView(viewsets.ViewSet):
    def list(self, request):
        """
        Получение списка рас
        """
        races = Race.objects.all()                
        serializer = RaceListSerializer(races, many=True)
        return Response({"races": serializer.data})

    def retrieve(self, request, pk=None):
        """
        Получение расы по идентификатору

        pk - идентификатор расы
        """
        queryset = Race.objects.all()
        race = get_object_or_404(queryset, pk=pk)
        serializer = RaceSerializer(race)        
        return Response(serializer.data)
