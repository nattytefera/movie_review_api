from rest_framework import serializers
from . import models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['id', 'title', 'genre', 'release_date', 'description']

class ReviewSerializer(serializers.ModelSerializer):
        movie = MovieSerializer(read_only=True)
        movie_id = serializers.PrimaryKeyRelatedField(
            queryset=models.Movie.objects.all(),
            source='movie',
            write_only=True
        )
        class Meta:
            model = models.Review
            fields = ['user', 'movie', 'rating', 'comment', 'created_at']
            read_only_fields = ['user', 'created_at']

        def validate_rating(self, value):
            if value < 1 or value > 5:
                 raise serializers.ValidationError("Rating must be between 1 and 5.")       
            return value
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
