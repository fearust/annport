from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from wedding import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wedding/', include('wedding.urls')),
    path('', views.wedding_index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
