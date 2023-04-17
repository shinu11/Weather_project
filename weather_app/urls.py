
from django.urls import  path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('<int:firstRequest>',views.home,name='home')
]
