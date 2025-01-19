# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('traveler.urls')),
#     path('trips/', include('trip.urls')),
# ]
#
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('trip.urls')),  # The index and trips routes
#     path('', include('traveler.urls')),  # Traveler profile routes
# ]

from django.contrib import admin
from django.urls import path, include

from traveler.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('trips/', include('trip.urls')),       # Routes like /trips/create/, /trips/<pk>/details/
    path('traveler/', include('traveler.urls')) # Routes like /traveler/create/, /traveler/details/
]
