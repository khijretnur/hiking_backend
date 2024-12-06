from months.views import MonthListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('months', MonthListView, basename='month-list-view')

urlpatterns = [

]

urlpatterns += router.urls
