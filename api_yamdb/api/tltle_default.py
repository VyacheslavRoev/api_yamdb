from django.shortcuts import get_object_or_404
from reviews.models import Title


class CustomTitleDefault:
    requires_context = True

    def __call__(self, serializer_field):
        title_id = serializer_field.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        return title
