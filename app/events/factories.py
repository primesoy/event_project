import factory 
import random
from django.utils import timezone
from datetime import datetime, timedelta
from user.factories import UserFactory
from . import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
        django_get_or_create = ("name",)
    
    name = factory.Iterator(["sport", "outdoor", "Pferdesport"])
    description = factory.Faker("paragraph", nb_sentences=3)


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event
    
    name = factory.Faker("sentence")
    author = factory.SubFactory(UserFactory)
    group_size = factory.LazyAttribute(
        lambda _: random.choice(list(models.Event.GroupSize.values))
    )
    category = factory.SubFactory(CategoryFactory)
    date = factory.Faker(
        "date_time_between",
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=100),
        tzinfo=timezone.get_current_timezone()          
        )

