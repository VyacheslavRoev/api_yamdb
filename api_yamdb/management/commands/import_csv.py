# import csv
# #import argparse
# #from django.core.management.base import BaseCommand # , CommandError

# # from reviews.models import Category, Genre, Title, TitleGenre


# #class Command(BaseCommand):
#     #help = 'Loads data from csv file.'

#     # def add_arguments(self, parser):
#     #     parser.add_argument('static/data', type=str)

# file_path = 'C:/Dev/api_yamdb/api_yamdb/static/data/category.csv'

# with open(file_path, 'r') as csv_file:
#     data = csv.reader(csv_file, delimiter=",")
#     for i, row in enumerate(data):
#         if i == 0:
#             print('This is the first line! Names for cols are:')
#             print(row)
#         else:
#             print('first: ' + row[0])
#             print('second: ' + row[1])
#             print('third: ' + row[2])
