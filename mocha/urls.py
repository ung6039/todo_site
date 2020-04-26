"""mocha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:   from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todo.views import todo_view
from todo.views import toto_su,delete_todo,todo_back

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todo_view,name="todos"),
    path('todos/',todo_view,name="todos"),
    path('todos/<pk>/in_progress/',toto_su, name="reload"),
    path('todos/<pk>/delete/',delete_todo,name="todo_del"),
    path('todos/<pk>/back/',todo_back,name="back")
]

