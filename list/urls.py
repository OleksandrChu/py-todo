from django.urls import path

from . import views

urlpatterns = [
    path('', views.todolists_page),
    path('create/', views.form_page),
    path('update/<int:id>/', views.form_update),
    path('update/', views.update),
    path('<int:id>/', views.get_by_id),
    # path('new_list/', views.create),
    # path('update/<int:id>/', views.update),
]
