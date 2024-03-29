"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import chatbot
from django.urls import include
from myapp.views import chat_view

urlpatterns = [
    path('', chat_view, name='chat'),
]

urlpatterns = [
    # ...
    path('chatbot/', include('django_chatterbot.urls', namespace='django_chatterbot')),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('get_response/', views.get_bot_response, name='get_bot_response'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('chatbot/', chatbot, name='chatbot'),
]


urlpatterns = [
    path("admin/", admin.site.urls),
]
