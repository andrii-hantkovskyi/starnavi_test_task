from django.urls import path

from analytics.views import LikeAnalyticsView, UserAnalyticsView

urlpatterns = [
    path('likes/', LikeAnalyticsView.as_view(), name='likes-analytic'),
    path('users/<int:pk>/', UserAnalyticsView.as_view(), name='user-analytic')
]
