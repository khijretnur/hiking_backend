from tags.views import TagListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('tags', TagListView)

urlpatterns = [

]

urlpatterns += router.urls
