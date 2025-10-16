from django.urls import path
from books import views 

urlpatterns = [ 
    path('example/', views.index, name='index'),
    path('example/about/', views.about, name='about'), 

    path('score', views.score_view, name='score_view'),

    #example visit url 8000/score/edit/5/ 
    #  > Django will extract score_id = 5
    #  > call the edit_score function in views.py and pass score_id 5 as arg

    path('score/edit/<int:score_id>/', 
         views.edit_score, name='edit_score'),

    path('score/delete/<int:score_id>/', 
         views.delete_score, name='delete_score'),
]