
from django.urls import path
from . import views
urlpatterns = [    
    path('', views.home, name= "home"),
    path('scores/', views.all_scores, name= "all_scores"),
    path('golfer/', views.all_golfers, name= "all_golfers"),
    path('add_scores/', views.add_scores, name= "add_scores"),
    path('add_golfer/', views.add_golfer, name= "add_golfer"),
]



