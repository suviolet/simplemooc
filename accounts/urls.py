from django.contrib.auth.views import LoginView
from django.urls import path
from accounts.views import register
#from accounts.views import login
#from django.conf.urls import include, url

app_name = 'accounts'

urlpatterns = [
    path(
        'entrar/', 
        LoginView.as_view(template_name='accounts/login.html'), 
        name='login'
    ),
    path(
        'cadastre-se/', register, name='register'
    ),
]
