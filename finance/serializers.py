from finance.models import *
from rest_framework import serializers

class FeeTermSerializers(serializers.ModelSerializer):

    class Meta:
        model = FeeTerm
        fields = ('__all__')



class FeeTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = FeeType
        fields = ('__all__')


class FeeGroupSerializers(serializers.ModelSerializer):

    class Meta:
        model = FeeGroup
        fields = ('__all__')