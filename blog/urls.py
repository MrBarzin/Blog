from django.urls import path
from .views import post_detail,PostListView,post_share,post_comment

app_name='blog'

urlpatterns =[
    path('',PostListView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
    path('share/<int:post_id>/',post_share,name='post_share'),
    path('comment/<int:post_id>',post_comment,name='post_comment')
]