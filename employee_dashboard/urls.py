
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

import employees.views

urlpatterns = [
    path('', views.signin , name='home'),
    path('employees/', include('employees.urls')),
    path('admin/', admin.site.urls),
    path('manager/manager_operations' ,  employees.views.manager_operations   ),
    path('manager/<str:username>/<str:status>' ,  employees.views.manager   ),
    path('manager/<str:username>/' ,  employees.views.manager   ),
    path('signout' ,  views.signout  ),
]


