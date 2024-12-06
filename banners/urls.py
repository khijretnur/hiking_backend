from banners.views import BannerListView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('banners', BannerListView)

urlpatterns = [

]

urlpatterns += router.urls
