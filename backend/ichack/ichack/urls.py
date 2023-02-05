"""ichack URL Configuration

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
from ichack.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ichack_view, name="ichack_view"),
    path("get_company/<int:comp_id>", request_get_company_for_id),
    path("get_roles/<int:comp_id>", request_get_roles_for_company),
    path("user_query/<str:text>", request_get_roles_for_user_query),
    path("users_for_role/<int:role_id>", request_get_users_for_roles),
    path("create_company/", request_post_create_new_company),
]
