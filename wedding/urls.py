from django.urls import path
from . import views

app_name = 'wedding'
urlpatterns = [
    path('detail/<int:mc_id>/', views.wedding_detail, name='wedding_detail'),
    path('list/', views.wedding_list, name='wedding_list'),
    path('cast/', views.wedding_cast, name='wedding_cast'),
    path('cast/success/', views.wedding_cast_success, name='wedding_cast_success')
]