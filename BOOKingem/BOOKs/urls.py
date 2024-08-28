from django.urls import path
from .views import main_home,context,kontakt

urlpatterns = [
    path('', main_home, name='main'),
    path('context/', context, name='context'),
    path('kontakt/', kontakt, name='kontakt'),
]