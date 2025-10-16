from django.urls import path
from books import views 

urlpatterns = [ 
    path('example/', views.index, name='index'),
    path('example/about/', views.about, name='about'), 
    
]