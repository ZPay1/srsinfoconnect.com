"""
URL configuration for SRSProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('', views.index_view, name='index'),
    path('header/', views.header_view, name='header'),
     path('About/', views.About_view, name='About'),
   
   
    path('Service/', views.Service_view, name='Service'),
    path('Seo/', views.Seo_view, name='Seo'),
    path('Web-design/', views.Web_design_view, name='Web_design'),
    
    path('Why-Choose/', views.Why_Choose_view, name='Why_Choose'),
    path('Portfolio/', views.Portfolio_view, name='Portfolio'),
    path('Contact-us/', views.Contact_view, name='Contact'),
    
    # path('Web-hoisting', views.Web_hoisting, name='Web_hoisting'),
    #  path('demo/', views.demo_view, name='demo'),
  
    
]
# Add this at the end of urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)