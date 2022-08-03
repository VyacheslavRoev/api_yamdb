from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from rest_framework.pagination import PageNumberPagination

from api.permissions import (ReviewCommentPermissions, IsAdminOrReadOnly)
from reviews.models import Category, Genre, Title, Review
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer, TitleReadOnlySerializer,
                             ReviewSerializer, CommentSerializer)
from api.mixins import ListCreateDestroyViewSet
from api.filters import TitleFilter


class CategoryViewSet(ListCreateDestroyViewSet):
    """Представление для категорий. Позволяет получить список категорий,
    информацию о них."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(ListCreateDestroyViewSet):
    """Представление для жанров. Позволяет получить список жанров,
    информацию о них."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    """Представление для произведений. Позволяет получить список произведений,
    информацию о них."""
    queryset = Title.objects.all().annotate(
        rating=Avg('reviews__score')).order_by('name')
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination
    ordering_fields = ('name')

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadOnlySerializer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Представление для отзывов.
    Позволяет получить список отзывов к произведениям,
    информацию о них."""
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = (ReviewCommentPermissions, )

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для комментариев.
    Позволяет получить список комментариев к отзывам,
    информацию о них."""
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = (ReviewCommentPermissions, )

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)
