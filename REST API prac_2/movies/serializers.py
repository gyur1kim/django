from .models import Actor, Movie, Review

from rest_framework import serializers

## 역참조를 위해 만든 serializers
# 1. 출연 영화 제목
class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', )

# 2. 출연 배우 이름
class ActorNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('name', )

# 3. 리뷰 목록
class ReviewSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content', )


######
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    movie_set = MovieTitleSerializer(many=True, read_only=True)
    movies = movie_set

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewSetSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'