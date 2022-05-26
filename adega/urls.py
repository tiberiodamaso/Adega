from django.urls import path
from .views import home, adega_criar

urlpatterns = [
    path('', home, name='home'),
    path('adega/criar/', adega_criar, name='adega_criar'),
]