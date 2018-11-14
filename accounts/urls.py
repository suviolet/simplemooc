from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import dashboard, register, edit, edit_password


app_name = 'accounts'

urlpatterns = [
    path(
        '', dashboard, name='dashboard'
    ),
    path(
        'entrar/', 
        LoginView.as_view(template_name='accounts/login.html'), 
        name='login'
    ),
    path(
        'sair/', LogoutView.as_view(next_page='/'),
        name='logout'
    ),
    path(
        'cadastre-se/', register, name='register'
    ),
    path(
        'editar/', edit, name='edit'
    ),
    path(
        'editar-senha/', edit_password, name='edit_password'
    ),
]