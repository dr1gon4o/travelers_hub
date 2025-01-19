from django.urls import path
from .views import (
    TripListView, TripCreateView, TripDetailView, TripUpdateView, TripDeleteView
)

urlpatterns = [
    # path('', TripListView.as_view(), name='index'),
    path('', TripListView.as_view(), name='all-trips'),
    path('create/', TripCreateView.as_view(), name='create-trip'),
    path('details/<int:pk>', TripDetailView.as_view(), name='details-trip'),
    path('edit/<int:pk>', TripUpdateView.as_view(), name='edit-trip'),
    path('delete/<int:pk>', TripDeleteView.as_view(), name='delete-trip'),
]
