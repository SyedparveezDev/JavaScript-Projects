from django.urls import path
from . import views

app_name = 'ipo_app'

urlpatterns = [
    # Web interface URLs
    path('', views.home, name='home'),
    path('ipos/', views.ipo_list, name='ipo_list'),
    path('ipo/<int:pk>/', views.ipo_detail, name='ipo_detail'),
    
    # API URLs
    path('api/', views.api_overview, name='api_overview'),
    path('api/ipo/', views.IPOListAPIView.as_view(), name='api_ipo_list'),
    path('api/ipo/<int:pk>/', views.IPODetailAPIView.as_view(), name='api_ipo_detail'),
]
