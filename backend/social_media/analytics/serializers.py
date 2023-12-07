from rest_framework import serializers


class LikeAnalyticsSerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()


class UserAnalyticsSerializer(serializers.Serializer):
    last_login = serializers.DateTimeField()
    last_request = serializers.DateTimeField()
