from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import urlpatterns
from .views import Post_viewset,User_viewset
from rest_framework.routers import SimpleRouter


# urlpatterns = [
#     path('',Post_list.as_view()),
#     path('<int:pk>/',Post_detail.as_view()),
#     path('users/',User_list.as_view()),
#     path('users/<int:pk>/',User_detail.as_view())
# ]   

router = SimpleRouter()
router.register('users',User_viewset,basename='users')
router.register('posts',Post_viewset,basename='posts')

urlpatterns = router.urls