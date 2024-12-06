from django.urls import path, include

urlpatterns = [
    path('', include('applications.urls')),
    path('', include('recommendations.urls')),
    path('', include('tags.urls')),
    path('', include('tours.urls')),
    path('', include('countries.urls')),
    path('', include('reviews.urls')),
    path('', include('services.urls')),
    path('', include('specialists.urls')),
    path('', include('documents.urls')),
    path('', include('months.urls')),
    path('', include('advantages.urls')),
    path('', include('banners.urls'))
]
