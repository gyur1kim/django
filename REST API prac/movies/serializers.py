from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


# 아래 ActorSerializer의 역참조를 위해 만든 클래스
class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', )

class ActorSerializer(serializers.ModelSerializer):
    # 여기서 출연한 영화에 대한 정보도 나오면 좋겠다~
    # 이 값이 영화 model에 들어있음 -> 역참조를 하자!!
    movie_set = MovieTitleSerializer(many=True, read_only=True)
    movies = movie_set

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


# 아래 MovieSerializer를 위한 클래스
class ActorNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('name', )

class ReviewSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content', )

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
        # 유효성 검사할 때 비어있으면 에러나잖아~ 오류 방지를 위해
        # read_only_fields 지정하주기
        read_only_fields = ('movie', )