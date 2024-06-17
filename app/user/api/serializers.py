from rest_framework import serializers
from django.contrib.auth import get_user_model   # wie in AUTH_USER_MODEL = "user.CustomUser" angegeben



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model() # das aktuelle User-Model
        fields = ("id", "email", "password", "user_name") #  "__all__"
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8},
        }
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    

    def update(self, instance, validated_data):
        print("validated:", validated_data)
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user
        
