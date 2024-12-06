from django.urls import path

from tours import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('tours', views.TourListView)
router.register('tours/detail', views.TourRetrieveView)
router.register('seasons', views.TourSeasonListView)
router.register('placements', views.TourPlacementListView)
router.register('formats', views.TourFormatListView)

urlpatterns = [
    path('tour-filter-data/', views.TourFilterDataAPI.as_view())
]

urlpatterns += router.urls
