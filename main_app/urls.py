from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('watches/', views.WatchList.as_view(), name='watches'),
    path('watches/<int:pk>/', views.WatchDetail.as_view(), name='watch_detail'),
    path('watches/create', views.WatchCreate.as_view(), name='watch_create'),
    path('watches/<int:pk>/edit/', views.WatchUpdate.as_view(), name='watch_update'),
    path('watches/<int:pk>/remove/', views.WatchDelete.as_view(), name='watch_remove'),
    path('watches/<int:watch_id>/add_photo/', views.add_photo, name='add_photo'),
    path('watches/<int:watch_id>/photos/<int:photo_id>/remove', views.remove_photo, name='remove_photo'),
    path('watches/<int:watch_id>/add_service/', views.add_service, name='add_service'),

    path('accessories/', views.AccessoryList.as_view(), name='accessory_list'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name="accessory_detail"),
    path('accessories/create/', views.AccessoryCreate.as_view(), name="accessory_create"),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name="accessory_update"),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name="accessory_delete"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/add_photo/', views.add_profile_photo, name='add_profile_photo'),
    path('profile/photo/remove', views.remove_profile_photo, name='remove_profile_photo'),
]