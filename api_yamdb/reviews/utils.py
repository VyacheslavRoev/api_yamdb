from django.utils import timezone
from django.forms import ValidationError


def validate_year(year):
    if year > timezone.now().year:
        raise ValidationError(
            (f'Год выпуска {year} больше текущего!'),
            params={'year': year},
        )
