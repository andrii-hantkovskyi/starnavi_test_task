from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from analytics.serializers import LikeAnalyticsSerializer, UserAnalyticsSerializer
from analytics.services.likes import get_date_ranged_likes
from users.services.common import get_all_users


class LikeAnalyticsView(generics.ListAPIView):
    serializer_class = LikeAnalyticsSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if not all((date_from, date_to)):
            return Response(status=HTTP_400_BAD_REQUEST, data={'detail': 'Not all params presented'})

        return get_date_ranged_likes(date_from, date_to)


class UserAnalyticsView(generics.RetrieveAPIView):
    serializer_class = UserAnalyticsSerializer
    queryset = get_all_users()
    permission_classes = (IsAdminUser,)
