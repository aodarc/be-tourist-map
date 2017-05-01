from django.contrib.gis.db import models
from django.contrib.gis.db.models import Avg

# Create your models here.
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)

from apps.core.base_models import BaseTimeCreateModifyModel
from apps.core.utils import upload_directory_path

MARKER_TYPE_CHOICE = (
    ('hotel', 'Готель'),
    ('cafe', 'Заклад харчування'),
    ('monument', "Архітектурна пам'ятка"),
    ('other', 'Інше')
)


class Marker(BaseTimeCreateModifyModel):
    position = models.PointField(verbose_name='Місце розташування')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    type = models.CharField(max_length=15, choices=MARKER_TYPE_CHOICE, db_index=True, default='other')
    main_img = models.ImageField(verbose_name='Головне зображення', upload_to='markers/')
    description = models.TextField(verbose_name='Опис', max_length=1600)
    address = models.CharField(max_length=255, verbose_name='Адреса')

    # history

    @property
    def ratting(self):
        return self.comments.aggregate(Avg('rating'))

    def __str__(self):
        return 'ID:{} T: {}'.format(self.id, self.title[:10])


class Comment(BaseTimeCreateModifyModel):
    user = models.ForeignKey('tmuser.User', related_name='comments')
    marker = models.ForeignKey(Marker, related_name='comments')
    rating = models.IntegerField(verbose_name='Рейтинг',
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    text = models.TextField(max_length=600, verbose_name='Коментар')

    def __str__(self):
        return 'User:{} Marker: {}'.format(self.user.get_full_name(), self.marker_id)


class Photo(BaseTimeCreateModifyModel):
    image = models.ImageField(verbose_name='Зображення', upload_to=upload_directory_path)
    owner = models.ForeignKey(to='tmuser.User', related_name='photos')
    marker = models.ForeignKey(Marker, related_name='photos')

    def __str__(self):
        return 'Marker: {} PhotoID: {}'.format(self.marker_id, self.id)
