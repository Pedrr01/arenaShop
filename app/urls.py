"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from Store.views import ProductListView, ProductCreate, ProductDetailView, ProductUpdateView, ProductDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('list/', ProductListView.as_view(), name='list_products'),
    path('create/', ProductCreate.as_view(), name='create_products'),
    path('product/<int:pk>/detail', ProductDetailView.as_view(), name='detail_products'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='update_products'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
