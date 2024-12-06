from recommendations import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('categories', views.RecommendationCategoryListView)
router.register('exclude', views.RecommendationExcludeView)
router.register('recommendation', views.RecommendationRetrieveView)

urlpatterns = [

]

urlpatterns += router.urls
