from django.db import models
from django.db.models.functions import Lower
from django.contrib.auth import get_user_model

from core.mixins import DatetimeMixin


User = get_user_model()


class Category(DatetimeMixin):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        ordering = [Lower("name")]
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def __str__(self):
        return self.name


class Event(DatetimeMixin):

    class GroupSize(models.IntegerChoices):
        BIG = 20
        SMALL = 10
        UNLIMITED = 0

    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    group_size = models.IntegerField(choices=GroupSize.choices)

    # on_delete:
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               related_name="events")  # user.events.all()

    category = models.ForeignKey(Category, 
                    on_delete=models.CASCADE, 
                    related_name="events")  # sport.events.all()