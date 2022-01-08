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


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'contact','profile_image','father_name','roles','mother_name','dob','address','pin_code','username','gender','enrollment_id','contact','password')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()]
            }
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        # role = Role.objects.get(id=5)
        # user['roles'] = role
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.profile_image = validated_data.get(
            'profile_image', instance.profile_image)
        instance.contact = validated_data.get(
            'contact', instance.contact)
        instance.dob = validated_data.get(
            'dob', instance.dob)
        instance.address = validated_data.get(
            'address', instance.address)
        instance.pin_code = validated_data.get(
            'pin_code', instance.pin_code)
        instance.save()
        return instance


class UserSerializerDetailed(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')


class UserDetailed(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'contact','gender', 'password','profile_image','father_name','mother_name','dob','address','pin_code','username','enrollment_id','contact')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')



class UserCreateSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'contact','gender','profile_image','father_name','dob','address','pin_code','username','contact','password')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()]
            }
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        # role = Role.objects.get(id=5)
        # user['roles'] = role
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):

        instance.name = validated_data.get(
            'name', instance.name)
        instance.profile_image = validated_data.get(
            'profile_image', instance.profile_image)
        instance.contact = validated_data.get(
            'contact', instance.contact)
        instance.dob = validated_data.get(
            'dob', instance.dob)
        instance.address = validated_data.get(
            'address', instance.address)
        instance.pin_code = validated_data.get(
            'pin_code', instance.pin_code)
        instance.save()
        return instance
