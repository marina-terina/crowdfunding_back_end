from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(f"{validated_data=}")
        return CustomUser.objects.create_user(**validated_data)
    
    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #     if password:
    #         instance.set_password(password)
