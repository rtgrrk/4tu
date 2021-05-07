from . import models

from rest_framework import serializers


class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.product
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
            'title',
            'image',
            'description',
            'price',
        )


class cartSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.cart
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
        )


class orderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.order
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
            'status',
        )
