from applications.views import ApplicationCreateView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('applications', ApplicationCreateView)

urlpatterns = [

]

urlpatterns += router.urls
