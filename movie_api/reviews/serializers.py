from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['id', 'title', 'genre', 'release_date', 'description']

class ReviewSerializer(serializers.ModelSerializer):
        movie = MovieSerializer(read_only=True)
        movie_id = serializers.PrimaryKeyRelatedField(
            queryset=models.Movie.objects.all(),
            source='movie',
            write_only=False,
            allow_null=False,
            style={'base_template': 'input.html'}
        )
        class Meta:
            model = models.Review
            fields = ['id','user', 'movie', 'movie_id', 'rating', 'comment', 'created_at']
            read_only_fields = ['user', 'created_at', 'movie']

        def validate_rating(self, value):
            if value < 1 or value > 5:
                 raise serializers.ValidationError("Rating must be between 1 and 5.")       
            return value
        
        def validate(self, data):
            if models.Review.objects.filter(
                user=self.context['request'].user,
                movie=data.get('movie')
            ).exists():
                raise serializers.ValidationError("You've already reviewed this movie.")
            return data
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
