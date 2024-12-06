from countries.views import CountryListView, SimpleCountryListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('countries', CountryListView)
router.register('country-list', SimpleCountryListView)

urlpatterns = [

]

urlpatterns += router.urls
