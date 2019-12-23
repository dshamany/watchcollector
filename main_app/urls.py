from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('watches/', views.WatchList.as_view(), name='watches'),
    path('watches/<int:pk>/', views.WatchDetail.as_view(), name='watch_detail'),
    path('watches/create', views.WatchCreate.as_view(), name='watch_create'),
    path('watches/<int:pk>/edit/', views.WatchUpdate.as_view(), name='watch_update'),
    path('watches/<int:pk>/delete/', views.WatchDelete.as_view(), name='watch_delete'),
    path('watches/<int:watch_id>/add_photo/', views.add_photo, name='add_photo'),

    path('accessories/', views.AccessoryList.as_view(), name="accessory_list"),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name="accessory_detail"),
    path('accessories/create/', views.AccessoryCreate.as_view(), name="accessory_create"),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name="accessory_update"),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name="accessory_delete"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]