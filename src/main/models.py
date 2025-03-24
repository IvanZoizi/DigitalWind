from django.db import models
from django.urls import reverse


class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='static/img', verbose_name='Изображения')
    description = models.CharField(max_length=500, verbose_name='Описание')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts', args=[str(self.title)])