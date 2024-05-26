from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['ID', 'email', 'name', 'password', 'generation', 'gender']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if User.objects.filter(ID=validated_data['ID']).exists():
            raise serializers.ValidationError("ID already exists.")
        
        user = User(
            email=validated_data['email'],
            ID=validated_data['ID'],
            name=validated_data['name'],
            generation=validated_data.get('generation'),
            gender=validated_data.get('gender')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
