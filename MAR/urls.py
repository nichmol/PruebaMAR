from django.contrib import admin
from django.urls import path, include
from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('autodiagnostico/', views.autodiagnostico, name='autodiagnostico'),
    path('plan/', views.plan, name='plan'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
