from django.urls import path 
from main.views import *

urlpatterns = [
    path('',index,name = 'posts'),
    path('detail_post/<int:post_id>/', detail_post, name = 'detail_post'),
    path('create_post/', create_post, name='create_post'),
    path('update_post/<int:post_id>/', update_post, name = 'update_post'),   
    path('delete_post/<int:post_id>/', delete_post, name = 'delete_post')
]



