from rest_framework.routers import DefaultRouter
from advantages import views

router = DefaultRouter()

router.register('advantages', views.AdvantageListView, basename='advantages-list-view')

urlpatterns = [

]

urlpatterns += router.urls
