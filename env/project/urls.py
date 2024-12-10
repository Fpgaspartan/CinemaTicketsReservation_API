
from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter
from tickets.views import GuestViewSet, MovieViewSet, ReservationViewSet

router=DefaultRouter()
router.register(r'Guest',GuestViewSet)
router.register(r'Movies',MovieViewSet)
router.register(r'Reservations',ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_page/', views.FBV_List),#FBV_one
    path('test_page_one/<int:pk>/', views.FBV_one),
    path('pages/', include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
]

