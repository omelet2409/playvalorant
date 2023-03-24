"""mysite URL Configuration

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
from django.urls import path, include

from home import views as home
from home.views.agents_view import AgentListView
from home.views.map_view import MapListView
from home.views.weapons_view import WeaponListView
from home.views.home_view import HomeListView
from home.views.specs_view import SpecsListView
from home.views.roles_view import RoleListView
from home.views.news_view import NewsListView
from home.views.agents_view import AgentDetailView

app_name = "home"

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path(
        route='',
        view = HomeListView.as_view(),
        name='home',
    ),
    path(
        route='agents/',
        view = AgentListView.as_view(),
        name='agents',
    ),
    path(
        route='maps/',
        view = MapListView.as_view(),
        name = 'maps',
    ),
    path(
        route='weapons/',
        view = WeaponListView.as_view(),
        name = 'weapons',
    ),
    path(
        route='specs/',
        view = SpecsListView.as_view(),
        name = 'specs',
    ),
    path(
        route='roles/',
        view = RoleListView.as_view(),
        name = 'roles',
    ),
    path(
        route = 'news/',
        view = NewsListView.as_view(),
        name = 'news',
    ),
    path(
        route = 'agent/<str:slug>/',
        view = AgentDetailView.as_view(),
        name = 'agent_detail',
    ),
    
    
]
