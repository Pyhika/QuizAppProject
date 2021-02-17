from django.urls import path
from .views import signupview, loginview, topview, logoutview

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('top/', topview, name='top'),
    path('logout/', logoutview, name='logout'),
]
