from django.urls import path
from simplemooc.views import home, contact

app_name = 'simplemooc'

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
]
