# import csv
# from django.core.management.base import BaseCommand, CommandError

# from reviews.models import Category, Genre, Title, TitleGenre #, Review, Comments, Users


# class Command(BaseCommand):
#     help = 'Loads data from csv file.'

#     def add_arguments(self, parser):
#         parser.add_argument('static/data', type=str)

#     def handle(self, *args, **options):
#         file_path = options['static/data']
#         with open(file_path, 'r') as csv_file:
#             data = csv.reader(csv_file, delimiter=",")
#             next(data, None)
#             for row in data:
#                 category = Category.objects.create(
#                     id=row['id'],
#                     name=row['name'],
#                     slug=row['slug']
#                 )
#                 genre = Genre.objects.create(
#                     id=row['id'],
#                     name=row['name'],
#                     slug=row['slug']
#                 )

