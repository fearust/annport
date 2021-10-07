from django.urls import path
from . import views

app_name = 'wedding'
urlpatterns = [
    path('', views.wedding_index, name='wedding_index'),
    path('service/', views.wedding_service, name='wedding_service'),
    path('detail/<int:mc_id>/', views.wedding_detail, name='wedding_detail'),
    path('list/', views.wedding_list, name='wedding_list'),
    path('cast/', views.wedding_cast, name='wedding_cast'),
    path('cast/success/', views.wedding_cast_success, name='wedding_cast_success'),
    path('partners/etland/', views.partners, name='partners')
]