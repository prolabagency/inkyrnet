from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from redactor.fields import RedactorField


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
    likes = models.IntegerField(default=0, verbose_name="Рейтинг")
    bookmark = models.ManyToManyField(User, verbose_name='В избранное', related_name='user_bookmark', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    edited_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='user_articles')

    def get_absolute_url(self):
        return '%s-%s' % (self.pk, self.slug)

