from django.urls import path,include
from .views import *

from .views.list_user_view import ListUserView
from .views.user_details_view import UserDetailsView

app_name = 'api'
urlpatterns = [
    path('api/v1/tweet/', ListCreateTweetView.as_view(), name='create'),
    path('api/v1/tweet/likes/', CreateDeleteLikeView.as_view(), name='like'),
    path('api/v1/tweet/comments/', CreateCommentView.as_view(), name='comment_create'),
    path('api/v1/tweet/comments/<int:pk>/', ListUpdateDeleteCommentView.as_view(), name='comment_details'),
    path('api/v1/tweet/public/', ListPublicTweetsView.as_view(), name='public_tweets'),
    path('api/v1/tweet/<int:pk>/', ListUpdateDeleteTweetView.as_view(), name='details'),
    path('api/v1/users/', ListUserView.as_view(), name='users'),
    path('api/v1/users/<int:pk>/', UserDetailsView.as_view(), name='user_detail'),
    path('accounts/', include('rest_registration.api.urls')),
]