from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    # path('tmdb/search/', tmdb_search, name='tmdb-search'),
    # path('api/register/', RegisterView.as_view(), name='register'),
] + router.urls