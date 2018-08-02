from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from redactor.fields import RedactorField


class Company(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'company'
        verbose_name = "компания"
        verbose_name_plural = "Компании"

    name = models.CharField(max_length=200, verbose_name="Заголовок")
    logo = models.FileField(verbose_name="Изображение")
    site = models.URLField(verbose_name="Сайт")
    description = RedactorField(verbose_name="Описание", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True,)
    email = models.EmailField(verbose_name="Электронная почта", blank=True)
    staff = models.ManyToManyField(User, verbose_name="Сотрудники", related_name="company_staff", blank=True)
    likes = models.IntegerField(default=0, verbose_name="Рейтинг")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    edited_at = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='user_company')

    def get_absolute_url(self):
        return '/%s' % self.slug


class Article(models.Model):
    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'article'
        verbose_name = "статью"
        verbose_name_plural = "Статьи"

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.FileField(verbose_name="Изображение")
    description = RedactorField(verbose_name="Описание")
    tags = TaggableManager(verbose_name='Теги', blank=True)
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slide = models.BooleanField(verbose_name="Слайдер", default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания',
                                related_name='company_articles', blank=True, null=True)
    likes = models.IntegerField(default=0, verbose_name="Рейтинг")
    bookmark = models.ManyToManyField(User, verbose_name='В избранное', related_name='user_bookmark', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    edited_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='user_articles')

    def get_absolute_url(self):
        return '%s-%s' % (self.pk, self.slug)

