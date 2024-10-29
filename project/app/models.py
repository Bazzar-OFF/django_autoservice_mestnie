from django.db import models

'''
category:
===========
title, slug,

service
==========
title, description, photo, category, slug

demo product
===========
title, description, photo, slug

demo users
===========
firs name, last name, photo, email, phone, slug

reviews
==========
name, post, photo, comment, 
mb slug

main_img
==========
name, photo

'''


class Category(models.Model):
    title = models.CharField(max_length=15, verbose_name='Название категории')
    photo = models.ImageField(upload_to='img/category/%Y/%m/%d/', blank=True, verbose_name='Фото')
    slug = models.SlugField(max_length=100, verbose_name='url_category', unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

# =======================

class Service(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='img/service/%Y/%m/%d/', blank=True, verbose_name='Фото')
    slug = models.SlugField(max_length=100, verbose_name='url_service', unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='services', verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


# ==========================

class Reviews(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    review = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(verbose_name="Дата создания комментария", auto_now_add=True)
    # slug = models.SlugField(max_length=100, verbose_name='url_reviews', unique=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']



