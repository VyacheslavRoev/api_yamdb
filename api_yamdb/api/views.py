from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from reviews.models import Category, Genre, Title  # , Comment, Review
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer, TitleReadOnlySerializer)
from api.mixins import ListCreateDestroyViewSet
from api.filters import TitleFilter


class CategoryViewSet(ListCreateDestroyViewSet):
    """Представление для категорий. Позволяет получить список категорий,
    информацию о них."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAdminOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(ListCreateDestroyViewSet):
    """Представление для жанров. Позволяет получить список жанров,
    информацию о них."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = (IsAdminOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    """Представление для произведений. Позволяет получить список произведений,
    информацию о них."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # permission_classes = (IsAdminOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadOnlySerializer
        return TitleSerializer
