from rest_framework import serializers
from django.contrib.auth.models import User
from authentication.models import Datasource, Datapoint


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, min_length=2)
    user_id = serializers.CharField(max_length=255, min_length=2)
    datasource_id = serializers.CharField(max_length=255, min_length=2)
    class Meta:
        model = Datapoint
        fields = ['name', 'user_id','datasource_id']

    def validate(self, attrs):
        datasource_id = attrs.get('datasource_id', '')
        if Datapoint.objects.filter(datasource_id=datasource_id).exists():
            raise serializers.ValidationError(
                {'datasource_id': ('id is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return Datapoint.objects.create(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']