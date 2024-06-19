from django.core.exceptions import ValidationError
from django.utils import timezone 


def date_in_past(field_value) -> None:
    if field_value <= timezone.now():
        raise ValidationError("Datum darf nicht in der Verhangenheit liegen")
