from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class TokenUserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer()
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'name', 'contact', 'password')
#         extra_kwargs = {
#             'username': {
#                 'validators': [UnicodeUsernameValidator()], 'password': {'write_only': True}
#             }
#         }

#     def create(self, validated_data):
#         user = super().create(validated_data)
#         role = Role.objects.get(id=3)
#         user['roles'] = role
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

#     def update(self, instance, validated_data):

#         instance.name = validated_data.get(
#             'name', instance.name)
#         instance.profile_image = validated_data.get(
#             'profile_image', instance.profile_image)
#         instance.contact = validated_data.get(
#             'contact', instance.contact)

#         instance.save()
#         return instance


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'contact', 'password', 'lab_name',
                  'roles', 'email')
        extra_kwargs = {'password': {'write_only': True}}
