from django.urls import path
from .views import BaseRegisterView, BaseLoginView, BaseLogoutView

urlpatterns = [
    path('', BaseLoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', BaseLogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup')
]