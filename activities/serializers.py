from rest_framework import serializers
from submissions.serializers import SubmissionSerializer

class ActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    points = serializers.IntegerField()
    submissions = SubmissionSerializer(many=True, required=False)

