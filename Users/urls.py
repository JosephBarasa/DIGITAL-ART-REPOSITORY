from django.urls import path
from . import views

urlpatterns = [
    path('user_index/', views.user_index, name='user_index'),
    path('user_sign_up/', views.user_sign_up, name='user_sign_up'),
    path('user_sign_in/', views.user_sign_in, name='user_sign_in'),
    path('user_sign_out/', views.user_sign_out, name='user_sign_out'),
    path('user_profile_display/', views.user_dashboard, name='user_dashboard'),
    path('user_profile_edit/', views.user_profile_edit, name='user_profile_edit'),
    path('user_artists/', views.user_artists, name='user_artists'),
    path('user_galleries/', views.user_galleries, name='user_galleries'),
    path('user_events/', views.user_events, name='user_events'),
    path('user_about/', views.user_about, name='user_about'),
    path('user_contact/', views.user_contact, name='user_contact'),
    path('user_artist_profile_display/<int:artist_id>/', views.user_artist_profile_display, name='user_artist_profile_display'),
]