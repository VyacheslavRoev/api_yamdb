from rest_framework import filters
#from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Category, Genre
from api.serializers import CategorySerializer, GenreSerializer
from api.mixins import ListCreateDestroyViewSet


class CategoryViewSet(ListCreateDestroyViewSet):
    """Представление для категорий. Позволяет получить список категорий,
    информацию о них."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes =
    filter_backends = (filters.SearchFilter,)
    #filterset_fields = ('title',)
    search_fields = ('title',)
    pagination_class = LimitOffsetPagination


class GenreViewSet(ListCreateDestroyViewSet):
    """Представление для жанров. Позволяет получить список жанров,
    информацию о них."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    #permission_classes =
    filter_backends = (filters.SearchFilter,)
    #filterset_fields = ('title',)
    search_fields = ('title',)
    pagination_class = LimitOffsetPagination
