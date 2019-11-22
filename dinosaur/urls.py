from django.urls import path
from dinosaur import views
from django.conf.urls import include

urlpatterns = [
  path('api/dinosaur/', views.dinosaur_list),
  path('api/dinosaur/<int:pk>/', views.dinosaur_detail),
  path('users/', views.UserList.as_view()),
  path('users/<int:pk>/', views.UserDetail.as_view()),
  path('api-auth/', include('rest_framework.urls')),
]
