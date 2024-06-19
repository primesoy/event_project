from rest_framework import serializers
from events.models import Category, Event, Tag, MachineType


# $ curl http://127.0.0.1:8000/api/events/categories -H "Authorization: Token 044f242ea137e2d0dc3a2a51d786cc8921cf179f"
# curl http://127.0.0.1:8000/api/events/ -H "Authorization: Token 044f242ea137e2d0dc3a2a51d786cc8921cf179f" 

class MachineTypeSerializer(serializers.ModelSerializer):

    files = serializers.StringRelatedField(read_only=True, many=True)
    
    class Meta:
        model = MachineType
        fields = "__all__"


class TagInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):

    # StringRelatedField gibt die Tags als Text aus, zb. Outdoor
    # tags = serializers.StringRelatedField(
    #     many=True, read_only=True
    # )

    # Gibt die Tags als IDs aus:
    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=True
    # )

    tags = TagInlineSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "date",
            "group_size",
            "category",
            "author",
            "tags",
        )
    
    def validate_name(self, field_value):
        """
        Verhindern, dass im Feld name eine Zeichenkette eingetragen wird
        Schema: validate_<FELDNAME>
        """
        if isinstance(field_value, str) and "xyz" in field_value:
            raise serializers.ValidationError("die Zeichenkette xyz ist im Namen verboten!")

    def update(self, instance, validated_data):
        request = self.context['request']
        tags = request.data.get("tags")

        try:
            x = Tag.objects.create(name="3usertagname")
            
            if tags is not None and isinstance(tags, list):
                instance.tags.clear()
                instance.tags.add(*tags)  # add(1, 2, 3)
                instance.tags.add(x)
        except Exception:
            pass
        
        return super().update(instance, validated_data)
    

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