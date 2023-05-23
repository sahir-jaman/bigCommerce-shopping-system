from .import views


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name = 'home'),
    path('index/', views.HOME, name = 'home'),
    path('base/', views.BASE, name ='base'),
    path('products/', views.PRODUCT, name='products'),
    path('search/', views.SEARCH, name='search'),
    path('contact/', views.Contact_Page, name='contact')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
