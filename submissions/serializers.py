from rest_framework import serializers


class SubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    grade = serializers.IntegerField(allow_null=True)
    repo = serializers.CharField()
    user_id = serializers.IntegerField()
    activity_id = serializers.IntegerField()