from django.contrib.gis.db import models
from django.contrib.gis.db.models import Avg

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.core.base_models import BaseTimeCreateModifyModel

MARKER_TYPE_CHOICE = (
    ('hotel', 'Готель'),
    ('cafe', 'Заклад харчування'),
    ('monument', "Архітектурна пам'ятка"),
    ('other', 'Інше')
)


class Country(models.Model):
    country = models.CharField(max_length=30, db_index=True)


class City(models.Model):
    city = models.CharField(max_length=30, db_index=True)
    country = models.ForeignKey(Country, related_name='cities')


class Marker(BaseTimeCreateModifyModel):
    position = models.PointField(verbose_name='Місце розташування')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    type = models.CharField(max_length=15, choices=MARKER_TYPE_CHOICE, db_index=True, default='other')
    main_img = models.ImageField(verbose_name='Головне зображення', upload_to='markers/')
    description = models.TextField(verbose_name='Опис', max_length=1600)
    city = models.ForeignKey(City, related_name='markers')
    country = models.ForeignKey(Country, related_name='markers')
    address = models.CharField(max_length=255, verbose_name='Адреса')

    # history

    @property
    def ratting(self):
        return self.comments.aggregate(Avg('rating'))


class Comments(BaseTimeCreateModifyModel):
    user = models.ForeignKey('tmuser.User', related_name='comments')
    marker = models.ForeignKey(Marker, related_name='comments')
    rating = models.IntegerField(verbose_name='Рейтинг',
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    text = models.TextField(max_length=600, verbose_name='Коментар')
