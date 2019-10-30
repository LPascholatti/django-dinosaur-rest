# from rest_framework import routers
# from .viewsets import DinosaurViewSet

# router = routers.DefaultRouter()
# router.register('api/dinosaur', DinosaurViewSet, 'dinosaur')

# urlpatterns = router.urls

#path('api/dinosaur/<int:pk>/', views.dinosaur_detail)

from django.urls import path
from dinosaur import views

urlpatterns = [
  path('api/dinosaur/', views.dinosaur_list),
  path('api/dinosaur/<int:pk>/', views.dinosaur_detail)
]
