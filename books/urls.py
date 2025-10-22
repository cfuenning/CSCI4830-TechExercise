from django.urls import path
from books import views 

urlpatterns = [ 
    path('', views.front_page, name='index'),
    path('about/', views.about, name='about'), 
    path('add/', views.create_book, name='create_book'),
    path('search/', search_list, name='search_list'),

    path('book', views.library_view, name='library_view'),

    #example visit url 8000/book/edit/5/ 
    #  > Django will extract book_id = 5
    #  > call the edit_book function in views.py and pass book_id 5 as arg

    path('book/edit/<int:book_id>/', 
         views.edit_book, name='edit_book'),

    path('book/delete/<int:book_id>/', 
         views.delete_book, name='delete_book'),
]