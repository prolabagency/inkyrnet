from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from magazine.models import Company
from magazine.models import Categories


class City(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'
        verbose_name = "Город"
        verbose_name_plural = "Города"

    name = models.CharField(max_length=200, verbose_name="Названия")
    slug = models.SlugField(verbose_name="Ярлык", unique=True)


class Location(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'location'
        verbose_name = "Место проведения"
        verbose_name_plural = "Место проведении"

    name = models.CharField(max_length=200, verbose_name="Названия")
    description = models.TextField(verbose_name="Описание")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='location_city', verbose_name="Город")
    map = models.CharField(max_length=250, verbose_name="Карта")
    site = models.URLField(verbose_name="Сайт")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)


class Event(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'event'
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Выбирите категорию")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.FileField(verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    tags = TaggableManager(verbose_name='Теги', blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано?")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='events_location',
                                 verbose_name="Место проведения")
    date_start = models.DateTimeField(verbose_name="Начало")
    date_end = models.DateTimeField(verbose_name="Конец")
    is_all_day = models.BooleanField(default=False, verbose_name="Мероприятие на весь день")
    is_paid = models.BooleanField(default=False, verbose_name="Платный?")
    price = models.CharField(max_length=50, verbose_name="Цена")
    is_premium_event = models.BooleanField(verbose_name="Премиум события?", default=False)
    is_going = models.IntegerField(verbose_name="Не иду/Иду", null=True, blank=True)
    site = models.URLField(verbose_name="Сайт")
    company = models.ManyToManyField(Company, verbose_name='Организаторы', related_name='event_company')
    bookmark = models.ManyToManyField(User, verbose_name='В избранных', related_name='user_bookmark_event', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    edited_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='user_event')
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def get_absolute_url(self):
        return '%s-%s' % (self.pk, self.slug)
