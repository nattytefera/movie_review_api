from rest_framework import viewsets, permissions 
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def tmdb_search(request):
    query = request.query_params.get('query', '')
    
    if not query:
        return Response({"error": "Add ?query=YourMovieTitle to the URL"}, status=400)
    
    try:
        response = requests.get(
            f"{settings.TMDB_BASE_URL}/search/movie",
            params={
                "api_key": settings.TMDB_API_KEY,
                "query": query,
                "language": "en-US"
            }
        )
        response.raise_for_status()  # Raises an error for bad status codes
        return Response(response.json().get("results", []))
    
    except requests.exceptions.RequestException as e:
        return Response({"error": f"TMDB request failed: {str(e)}"}, status=500)
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.select_related('movie').filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)