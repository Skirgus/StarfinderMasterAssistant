from django.urls import path
from .views import RacesView, ThemeView, GameClassView, CharacterView, WorldsView, LanguageView, WeaponView, ArmorView
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
    path('worlds/', WorldsView.as_view({'get': 'list'})),
    path('worlds/<int:pk>', WorldsView.as_view({'get': 'retrieve'})),
    path('language/', LanguageView.as_view({'get': 'list'})),
    path('language/<int:pk>', LanguageView.as_view({'get': 'retrieve'})),
    path('characters/', CharacterView.as_view({'get': 'list'})),
    path('characters/<int:pk>', CharacterView.as_view({'get': 'retrieve'})),
    path('characters/', CharacterView.as_view({'post': 'post'})),
    path('characters/<int:pk>', CharacterView.as_view({'put': 'put'})),    
    path('characters/<int:pk>/character_blank', CharacterView.as_view({'get': 'character_blank'})),
    path('login/', login),
    path('weapons/', WeaponView.as_view({'get': 'list'})),
    path('weapons/<int:pk>', WeaponView.as_view({'get': 'retrieve'})), 
    path('armors/', ArmorView.as_view({'get': 'list'})),
    path('armors/<int:pk>', ArmorView.as_view({'get': 'retrieve'})) 
]