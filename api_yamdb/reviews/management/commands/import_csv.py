import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from reviews.models import Category, Genre, Title, TitleGenre, Comment, Review, User

DICT = {
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    User: 'users.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
    TitleGenre: 'genre_title.csv'
}


class Command(BaseCommand):
    help = 'Loads data from csv file.'

    def handle(self, *args, **kwargs):
        for model, file in DICT.items():
            with open(f'{settings.BASE_DIR}/static/data/{file}', 'r',
                      encoding='utf-8') as csv_file:
                data_reader = csv.DictReader(csv_file, delimiter=",")

                for row in data_reader:
                    #print(row)
                    model.objects.bulk_create(model(**data) for data in data_reader)
        self.stdout.write("Команда выполнена")





