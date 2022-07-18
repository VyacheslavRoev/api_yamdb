from rest_framework import viewsets, mixins
#from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """Представление для категорий. Позволяет получить список категорий,
    информацию о них."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ('title',)
    pagination_class = LimitOffsetPagination
