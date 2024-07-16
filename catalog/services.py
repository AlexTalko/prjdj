from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_category_list_from_cache():
    """
    Метод получения списка категорий из кэша(хранится 60мин) или из базы данных
    """
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    category_list = cache.get(key)
    if category_list is not None:
        return category_list
    category_list = Category.objects.all()
    cache.set(key, category_list, 60*60)
    return category_list
