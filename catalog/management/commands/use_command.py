import json
from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        ''' Метод распаковки json-файла и сохранения в новый список для дальнейшей работы'''
        categories_list = []
        with open('catalog/fixtures/category.json', 'r') as f:
            file = json.load(f)

            for item in file:
                categories_list.append(item)
        return categories_list

    @staticmethod
    def json_read_products():
        ''' Метод распаковки json-файла и сохранения в новый список для дальнейшей работы'''
        products_list = []
        with open('catalog/fixtures/products.json', 'r') as f:
            file = json.load(f)

            for item in file:
                products_list.append(item)
        return products_list

    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE;")

        Product.objects.all().delete()
        Category.objects.all().delete()

        products_for_create = []
        categories_for_create = []

        for category_item in Command.json_read_categories():
            categories_for_create.append(
                Category(id=category_item['pk'],
                         name=category_item['fields']['name'],
                         description=category_item['fields']['description'],
                         )
            )

        Category.objects.bulk_create(categories_for_create)

        for product_item in Command.json_read_products():
            products_for_create.append(
                Product(id=product_item['pk'],
                        name=product_item['fields']['name'],
                        description=product_item['fields']['description'],
                        price=product_item['fields']['price'],
                        category=Category.objects.get(id=product_item['fields']['category']),
                        image=product_item['fields']['image'],
                        created_at=product_item['fields']['created_at'],
                        updated_at=product_item['fields']['updated_at'],
                        )
            )

        Product.objects.bulk_create(products_for_create)

        # Дополнительное задание 1
        print(Product.objects.all().order_by('-created_at')[:2])
