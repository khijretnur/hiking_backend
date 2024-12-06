from rest_framework.routers import DefaultRouter

from specialists.views import SpecialistViewSet

router = DefaultRouter()

router.register('specialists', SpecialistViewSet, basename='specialist-view-set')

urlpatterns = [

]

urlpatterns += router.urls
