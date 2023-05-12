from django.urls import path
from .views import PostList, PostDetail, PostUpdate, PostDelete, PostCreate, UserView, CommentCreate, CommentDelete


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
    path('account/', UserView.as_view(), name='user_view'),
    path('comment_create/', CommentCreate.as_view(), name='comment_create'),
    path('comment_delete/<int:pk>', CommentDelete.as_view(), name='comment_delete')
]
