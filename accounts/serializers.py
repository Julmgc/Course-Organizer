from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()

  