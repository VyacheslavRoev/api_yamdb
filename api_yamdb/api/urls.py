from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                       ReviewViewSet, CommentViewSet)
from custom_auth.views import (UserViewSet, registration, get_jwt_token)

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router_v1.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', registration, name='registration'),
    path('v1/auth/token/', get_jwt_token, name='jwt_token')
]
