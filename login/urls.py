from django.urls import path
from . import views 


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register_view/', views.register_view, name='register_view'),

]