from django.urls import path
from blog import views

APP_NAME = 'blog'

urlpatterns = [
   path('',
      views.PostListView.as_view(),
      name='post_list'),

   path('kinh-nghiem-ca-nhan/',
         views.Tag1ListView.as_view(),
         name='tag1_list'),

   path('chu-de-cong-nghe/',
         views.Tag2ListView.as_view(),
         name='tag2_list'),

   path('linh-tinh-ca-nhan/',
         views.Tag3ListView.as_view(),
         name='tag3_list'),

   path('Cong-cuoc-reviewer/',
         views.Tag4ListView.as_view(),
         name='tag4_list'),

   path('about/',
      views.AboutView.as_view(),
      name='about'),

   path('post/<int:pk>/',
         views.PostDetailView.as_view(),
      name='post_detail'),
      
   path('post/new/',
      views.CreatePostView.as_view(),
      name='post_new'),

   path('post/<int:pk>/edit/',
      views.PostUpdateView.as_view(),
      name='post_edit'),

   path('post/<int:pk>/remove/',
      views.PostDeleteView.as_view(),
      name='post_remove'),

   path('post/drafts/',
      views.DraftListView.as_view(),
      name='post_draft_list'),

   path('post/<int:pk>/comment/',
      views.add_comment_to_post,
      name='add_comment_to_post'),

   path('comment/<int:pk>/approve/',
      views.comment_approve,
      name='comment_approve'),

   path('comment/<int:pk>/remove/',
      views.comment_remove,
      name='comment_remove'),

   path('post/<int:pk>/publish',
      views.post_publish,
      name='post_publish'),
]
