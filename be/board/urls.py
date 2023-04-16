from django.urls import path
from . import views
from .views import board_info, board_actions

#  urlpatterns = [ 
#      path('', views.index, name='index'),
#  ]
urlpatterns = [
    path('', views.board_info, name='board_info'),
    path('details/', board_info), 
    path('details/<int:pk>/', board_info),
     
     ]