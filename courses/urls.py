from django.urls import path
from courses.views import index, details

app_name = 'courses'

urlpatterns = [
    path('', index, name='index'),
    # path('<int:pk>/', details, name='details'),
    path('<slug>/', details, name='details'),
]
