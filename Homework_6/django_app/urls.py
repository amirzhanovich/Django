
from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("pricing/", views.pricing),
    path("login/", views.login),
    path("signup/", views.signup),
    path("details/", views.details),

    # path("", views.home),

]
