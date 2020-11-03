from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.get_by_id),
    path('new_task/', views.create),
    path('update/<int:id>/', views.update),
]
