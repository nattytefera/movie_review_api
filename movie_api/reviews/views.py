from rest_framework import viewsets, permissions 
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
# Create your views here.

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