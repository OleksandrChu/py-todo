from django.urls import path

from . import views

urlpatterns = [
    path('', views.todolists_page),
    path('<int:id>/', views.todolist_page),
    path('update/<int:id>/', views.form_update),
    path('update/', views.update)
]
