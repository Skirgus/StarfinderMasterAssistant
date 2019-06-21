from django.urls import path
from .views import RacesView
from .authorization import login
app_name = "starfinder"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('races/', RacesView.as_view()),
    path('login/', login)
]