from rest_framework import serializers
from dashboard.models import *


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = SocialMedia
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class AboutProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProduct
        fields = "__all__"


class UnityProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnityProduct
        fields = "__all__"


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = "__all__"


class WhoUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoUse
        fields = "__all__"


class HowToUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowToUse
        fields = "__all__"


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = "__all__"