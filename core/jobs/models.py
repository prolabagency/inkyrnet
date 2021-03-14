from django.db import models
from django.contrib.auth.models import User
from magazine.models import Company
from magazine.models import Categories
from events.models import City

TYPE_TIME = (
    ('full-time', "Полная занятость"),
    ('temporary', "Временный"),
    ('internship', "Стажировка"),
    ('freelance', "Фриланс"),
    ('part-time', "	Частичная занятость"),
    ('another', "Другое"),
)


class TypeTime(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    type_time = models.CharField(choices=TYPE_TIME, max_length=30, verbose_name="Выберите время")
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "type_time"
        verbose_name = "Тип занятости"
        verbose_name_plural = "Типы занятости"


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "position"
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Technology(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "technology"
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"


class Job(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'job'
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='job_position',
                                 verbose_name="Выбирите должность")
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='job_technology',
                                   verbose_name="Выберите технологию")
    type_time = models.ForeignKey(TypeTime, on_delete=models.CASCADE, related_name='job_time',
                                  verbose_name="Выберите время")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    date_end = models.DateTimeField(verbose_name="Дата истечения")
    price_min = models.CharField(max_length=30, verbose_name="Цена минимум")
    price_max = models.CharField(max_length=30, verbose_name="Цена максимум")
    experience = models.IntegerField(verbose_name="Опыт(год)", default="1", blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='job_city', verbose_name="Город")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания работадатель',
                                related_name='job_company')
    is_closed = models.BooleanField(default=True, verbose_name="Вакансия закрыта?")
    is_premium_job = models.BooleanField(verbose_name="Премиум-вакансия?", default=False)
    bookmark = models.ManyToManyField(User, verbose_name='В избранных', related_name='user_bookmark_job', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    edited_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='user_job')
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def get_absolute_url(self):
        return 'job/%s-%s' % (self.pk, self.slug)
