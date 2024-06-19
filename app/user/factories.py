import factory 
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):
    """Eine Fabrik zum Anlegen eines zufälligen User-Objekts."""
    class Meta:
        model = get_user_model()
        django_get_or_create = ("user_name",)  # wenn es User gibt, lege nicht neu an!
    
    user_name = factory.Iterator(["bob", "alice", "john"])
    password = factory.LazyFunction(lambda: make_password("abc"))
    email = factory.Sequence(lambda n: f"user{n}@example.com")
