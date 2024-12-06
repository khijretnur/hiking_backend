from documents.views import DocumentViewSet, PrivacyStatementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('documents', DocumentViewSet, basename='document-view-set')
router.register('privacy-statements', PrivacyStatementViewSet, basename='privacy-statement-view-set')


urlpatterns = []

urlpatterns += router.urls
