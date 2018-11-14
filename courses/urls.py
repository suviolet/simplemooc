from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from courses.views import index, details
from django.conf import settings

app_name = 'courses'

urlpatterns = [
    path('', index, name='index'),
    # path('<int:pk>/', details, name='details'),
    path('<slug>/', details, name='details'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
