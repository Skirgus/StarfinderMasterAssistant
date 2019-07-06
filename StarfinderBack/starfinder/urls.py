from django.urls import path
from .views import RacesView, ThemeView, GameClassView, CharacterView
from .authorization import login
app_name = "starfinder"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('races/', RacesView.as_view({'get': 'list'})),
    path('races/<int:pk>', RacesView.as_view({'get': 'retrieve'})),
    path('themes/', ThemeView.as_view({'get': 'list'})),
    path('themes/<int:pk>', ThemeView.as_view({'get': 'retrieve'})),
    path('classes/', GameClassView.as_view({'get': 'list'})),
    path('classes/<int:pk>', GameClassView.as_view({'get': 'retrieve'})),
    path('characters/', CharacterView.as_view({'get': 'list'})),
    path('characters/<int:pk>', CharacterView.as_view({'get': 'retrieve'})),
    path('characters/', CharacterView.as_view({'post': 'post'})),
    path('login/', login)    
]