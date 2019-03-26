from django.urls import path, include
from lists import views
from django.contrib import admin

urlpatterns = [
    path('', views.home_page, name="home"),
    path('lists/', include('lists.urls')),
    path('accounts/', include('accounts.urls'))
]
