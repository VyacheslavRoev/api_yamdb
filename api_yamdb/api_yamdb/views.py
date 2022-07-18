from rest_framework import filters
#from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from .models import Category
from .serializers import CategorySerializer
from .mixins import ListCreateDestroyViewSet


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
