from rest_framework import serializers
from events.models import Category, Event


# $ curl http://127.0.0.1:8000/api/events/categories -H "Authorization: Token 044f242ea137e2d0dc3a2a51d786cc8921cf179f"
# curl http://127.0.0.1:8000/api/events/categories -H "Authorization: Token 044f242ea137e2d0dc3a2a51d786cc8921cf179f" 


class EventInlineSerializer(serializers.ModelSerializer):

    # Wenn man nicht die ID des ForeignKey-Objects haben will,
    # sondern 
    author = serializers.StringRelatedField()  # Name des Authors

    class Meta:
        model = Event
        fields = ("id", "name", "author")


class CategorySerializer(serializers.ModelSerializer):

    # events ist der related_name von dem Event-Model
    events = EventInlineSerializer(many=True, read_only=True) # nur Lesen!

    def to_representation(self, current_category):
        """In der Ausgabe für jede Instanz der Kategoie
        zusätzliche Felder ausgeben."""
        representation =  super().to_representation(current_category)
        representation["number_events"] = current_category.events.count()
        return representation

    class Meta:
        model = Category
        fields = "__all__"