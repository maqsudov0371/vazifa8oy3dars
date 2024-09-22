from django.urls import path
from .views import CarDetailView, BrandDetailView, OwnerDetailView

urlpatterns = [
    path('cars/', CarDetailView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('brands/', BrandDetailView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('owners/', OwnerDetailView.as_view(), name='owner-list'),
    path('owners/<int:pk>/', OwnerDetailView.as_view(), name='owner-detail'),
]
