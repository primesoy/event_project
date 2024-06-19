from django.core.management.base import BaseCommand

from events.factories import EventFactory
from events.models import Event

NUMBER_EVENTS = 300

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Event.objects.all().delete()
        print("Events deleted. creating events...")
        EventFactory.create_batch(NUMBER_EVENTS)
        print("Events created")