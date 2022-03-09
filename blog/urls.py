"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from  .import settings
from core.views import PostViewSet, ComentariViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register('post', PostViewSet)
router.register('comentari', ComentariViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('post/all/', views.list_all_post),
    path('post/user/', views.list_user_post),
    path('post/detail/<id>/', views.post_detail),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('post/register/', views.register_post),
    path('post/register/submit', views.set_post),
    path('post/delete/<id>/', views.delete_post),
    path('cadastrar_usuario/', views.cadastrar_usuario),
    path('post/comentar/<id>/', views.set_comment),
    path('post/comentar/<id>/submit', views.comentar),
    path('', RedirectView.as_view(url='post/all/')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)