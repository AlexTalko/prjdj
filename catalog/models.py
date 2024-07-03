from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="products/images", verbose_name="Изображение (превью)", blank=True, null=True
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    owner = models.ForeignKey(User, verbose_name="Продавец", help_text="Укажите продавца товара", blank=True, null=True,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Продукт",
        related_name="version_product",)

    number_version = models.CharField(default=0, verbose_name="Номер версии")
    name_version = models.CharField(max_length=100, verbose_name="Название версии")
    is_current = models.BooleanField(
        default=False, verbose_name="Признак текущей версии"
    )

    def __str__(self):
        return f"{self.product}, {self.number_version}, {self.name_version}"

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
