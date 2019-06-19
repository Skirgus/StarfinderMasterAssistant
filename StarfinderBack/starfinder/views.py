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
# Create your views here.
@api_view(["Get"])
def Races(request):
    try:
        race_array = []
        for raceFile in os.listdir("Races"):
            with open(os.path.join("Races", raceFile), 'r' , encoding="utf-8") as openRaceFile:
                race = json.load(openRaceFile)
                race_array.append(race)
        return JsonResponse(json.dumps(race_array), safe=False)        
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def Race_Info(request, name):
    try:
        with open(os.path.join("Races", name+'.json'), 'r' , encoding="utf-8") as openRaceFile:
            race = json.load(openRaceFile)
        return JsonResponse(json.dumps(race), safe=False)        
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)