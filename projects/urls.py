"""codelnmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path

from projects.views import project_list, project_view, categories_view, dev_type_view, project_type_view

app_name = 'projects'
urlpatterns = [
    path('<int:id>/', project_view, name='project'),
    path('all-projects/<int:id>/', project_list, name='all-projects'),
    path('dev-type/<slug:slug>/', dev_type_view, name='dev-type'),
    path('project-type/<slug:slug>/', project_type_view, name='project-type'),
    path('categories/', categories_view, name='categories'),

]
