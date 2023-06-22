from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import PersonalNoteViewSet

urlpatterns = [
  path('notes/', PersonalNoteViewSet.as_view({'get': 'list', 'post': 'create'})),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]