from django.shortcuts import render

from .serializers import ActorListSerializer, ActorSerializer
from .serializers import MovieListSerializer, MovieSerializer
from .serializers import ReviewListSerializer, ReviewSerializer
from .models import Actor, Movie, Review

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # update가 아니라 create니까 instance는 넣지 않습니다~
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 비어있던 movie field 채워주기
        serializer.save(movie=movie)
        return Response(status=status.HTTP_201_CREATED)