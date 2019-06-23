from django.urls import path
from .views import RacesView
from .authorization import login
app_name = "starfinder"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('races/', RacesView.as_view({'get': 'list'})),
    path('races/<int:pk>', RacesView.as_view({'get': 'retrieve'})),
    path('login/', login)
]