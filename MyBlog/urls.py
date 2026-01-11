"""
URL configuration for MyBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
import blog.views
#from blog.views import Home, new_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.Home.as_view(), name='home_page'),
    path('newPost/', blog.views.new_post, name='new_post'),
    path('list_posts/', blog.views.list_post.as_view(), name='list_posts'),
    path('detail_post/<int:id>/', blog.views.detail_post.as_view(), name='detail_post'),
    path('delete_post/<int:id>/', blog.views.delete_post.as_view(), name='delete_post'),
    path('edit_post/<int:id>/', blog.views.edit_post.as_view(), name='edit_post'),
    path('update_post/', blog.views.update_post, name='update_post'),
]
