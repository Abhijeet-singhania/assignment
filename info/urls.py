from django.conf.urls import url 
from django.urls import path, include 
from . import views

app_name = 'info'

urlpatterns = [
    
    path('add/', views.add_view, name="add"),
    path('filter/', views.filter_view, name="filter"),
    path('edit/<int:id>', views.edit,name="edit"),  
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.remove,name="remove"), 
    path('', views.home, name="home"),
    
]