from rest_framework import serializers


class GetTokensSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
