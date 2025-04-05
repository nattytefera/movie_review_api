from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet, tmdb_search
from django.urls import path

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('tmdb/search/', tmdb_search, name='tmdb-search'),
] + router.urls