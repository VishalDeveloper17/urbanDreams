from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('submit/', views.submit,name='submit'),
    path('resource/', views.resource, name='resource')
]