# Django import
from django.contrib import admin
from django.urls import path, include, re_path

from moove_apps.user import views
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
# local import

admin.site.site_header = 'Moove Africa'

urlpatterns = [
    path('', admin.site.urls),
    path('health/', views.HealthCheckView.as_view({'get': 'get'}), name='health_check'),
    path('api/driver/', include('moove_apps.driver.urls', namespace='driver')),
    path('api/users/', include('moove_apps.users.urls', namespace='users')),
]
