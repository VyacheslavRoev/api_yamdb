from rest_framework import filters, viewsets
#from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Category, Genre, Title
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer)
from api.mixins import ListCreateDestroyViewSet


class CategoryViewSet(ListCreateDestroyViewSet):
    """Представление для категорий. Позволяет получить список категорий,
    информацию о них."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes =
    filter_backends = (filters.SearchFilter,)
    #filterset_fields = ('name',)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination


class GenreViewSet(ListCreateDestroyViewSet):
    """Представление для жанров. Позволяет получить список жанров,
    информацию о них."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    #permission_classes =
    filter_backends = (filters.SearchFilter,)
    #filterset_fields = ('name',)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    #permission_classes = [IsAdminOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    # def get_serializer_class(self):
    #     if self.action in ['list', 'retrieve']:
    #         return TitleSerializerList
    #     return TitleSerializer
