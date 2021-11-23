from django.urls import path
from django.urls.resolvers import URLPattern
from .views import Post_list,Post_detail


urlpatterns = [
    path('',Post_list.as_view()),
    path('<int:pk>/',Post_detail.as_view()),
]   