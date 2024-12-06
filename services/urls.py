from services import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('services', views.ServiceViewSet)
router.register('service-exclude', views.ServiceExcludeList)

urlpatterns = [

]

urlpatterns += router.urls
