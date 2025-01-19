from django.urls import path

from . import views
from .views import (
    TravelerCreateView, TravelerUpdateView, TravelerDeleteView, IndexView, TravelerDetailView
)

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('create/', TravelerCreateView.as_view(), name='create-traveler'),
    path('details/', TravelerDetailView.as_view(), name='details-traveler'),
    # path('details/', views.TravelerDetailsView, name='details-traveler'),
    path('edit/', TravelerUpdateView.as_view(), name='edit-traveler'),
    path('delete/', TravelerDeleteView.as_view(), name='delete-traveler'),
]
