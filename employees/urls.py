from django.urls import path
from .import views

urlpatterns = [
    path('operations', views.operations, name='operations'),
    path('<str:username>/<str:status>', views.employees, name='employees'),
    path('<str:username>/', views.employees, name='employees'),

    
]
