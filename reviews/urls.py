from reviews.views import ReviewListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('reviews', ReviewListView)

urlpatterns = [

]

urlpatterns += router.urls
