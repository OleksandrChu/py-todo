from django.urls import path

from . import views

urlpatterns = [
    path('', views.todolists_page),
    path('create/', views.create_form),
    path('update/<int:id>/', views.form_update),
    path('update/', views.update),
    # path('<int:id>/', views.get_by_id),
]
