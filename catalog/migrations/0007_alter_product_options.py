# Generated by Django 4.2.13 on 2024-07-07 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "price"],
                "permissions": [
                    ("can_edit_product", "Может изменять продукт"),
                    ("can_edit_description", "Может изменять описание продукта"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
