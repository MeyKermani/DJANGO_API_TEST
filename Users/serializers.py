from rest_framework import serializers
from Users.models import CustomUser, Address


class AddressSerializer(serializers.ModelSerializer):
    user_uuid = serializers.UUIDField(source='user.uuid')

    class Meta:
        model = Address
        fields = ('user_uuid', 'title', 'latitude', 'longitude', 'creator')

    def create(self, validated_data):
        user = CustomUser.objects.get(uuid=validated_data['user']['uuid'])
        validated_data['user'] = user
        address = Address.objects.create(**validated_data)
        return address


class ShortUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        
        
        fields = ('first_name', 'last_name')


class FullUserSerializer(serializers.ModelSerializer):
    last_addresses = AddressSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'address_count', 'last_addresses')
