
from django.contrib import admin
from django.urls import path
from homepage import views
#from homepage.views import SiteContent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name="home"),
    path('home/', views.home , name="home"),
    path('contactus/', views.contact_us, name='contactus'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('suggessions/', views.suggessions , name='suggest'),
    path('home/All-About-A-Website/', views.All_About_A_Website, name='All_About_A_Website'),
    path('home/Cyber-Security/', views.Cyber_security, name='Cyber-Security'),
]
