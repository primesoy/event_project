from django.db import models
from django.db.models.functions import Lower
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

from core.mixins import DatetimeMixin
from .validators import date_in_past


User = get_user_model()


class MachineType(DatetimeMixin):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MachineTypeFile(DatetimeMixin):
    file = models.FileField(upload_to="machine_files")
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE, related_name="files")

    def __str__(self) -> str:
        return self.file.name


class PDFMOdel(DatetimeMixin):
    file = models.FileField(upload_to="files", blank=True, null=True)

    def __str__(self) -> str:
        return self.file.path  # self.file.name


class Category(DatetimeMixin):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(
        null=True,
        blank=True,
    )
    files = models.ManyToManyField(PDFMOdel, related_name="category")  # sport.files.all() 
    
    class Meta:
        ordering = [Lower("name")]
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    

class Event(DatetimeMixin):

    class GroupSize(models.IntegerChoices):
        BIG = 20
        SMALL = 10
        UNLIMITED = 0

    name = models.CharField(max_length=100, 
                            unique=True, 
                            validators=[
                                MinLengthValidator(3, message="Das ist zu kurz")
                            ]
    )
    date = models.DateTimeField(validators=[date_in_past])
    is_active = models.BooleanField(default=True)
    group_size = models.IntegerField(choices=GroupSize.choices)
    tags = models.ManyToManyField(Tag, related_name="events", blank=True)  # tag.events.all()
    # event.tags.all()

    # on_delete:
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               related_name="events")  # user.events.all()

    category = models.ForeignKey(Category, 
                    on_delete=models.CASCADE, 
                    related_name="events")  # sport.events.all()