from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('simplemooc.urls', namespace='simplemooc')), 
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('cursos/', include('courses.urls', namespace='courses')),
    path('admin/', admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
    