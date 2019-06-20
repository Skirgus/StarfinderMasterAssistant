# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import os
import codecs
from starfinder.dto import RaceListDto
# Create your views here.
@api_view(["Get"])
def Races(request):
    """ Возвращает список рас """
    try:
        race_array = []
        for raceFile in os.listdir("Races"):
            with codecs.open(os.path.join("Races", raceFile), 'r' , encoding="utf-8") as openRaceFile:
                race = openRaceFile.read()
                raceJson = json.loads(race, encoding='utf-8')
                race_array.append(RaceListDto(raceJson['id'], raceJson['name']).__dict__)
        return JsonResponse(race_array, safe=False)        
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def Race_Info(request, id):
    """
    Возвращает информацию по расе

        Keyword arguments:
            id -- идентификатор расы
    
    """
    try:
        with codecs.open(os.path.join("Races", id+'.json'), 'r', 'utf-8') as openRaceFile:
           race = openRaceFile.read()
           raceJson = json.loads(race, encoding='utf-8')
        return JsonResponse(raceJson, safe=False)        
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)