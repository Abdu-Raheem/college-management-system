from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .api.views.account_views import ProfileView, ProfileManagementView, ProfileListAPIView
from .api.views.groqviews import AIChatView

urlpatterns = [
    path('sample/', views.sample, name='sample'),
    path('my-name/', views.my_name, name='my_name'),
    path('order-list/', views.order_list, name='order_list'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('create-profile/', views.create_profile, name='create_profile'),
    # path('login/', views.login_user, name='login'),

    path('get-profiles/', ProfileView.as_view(), name='get_profiles'),
    path('get-profile/<int:id>/', ProfileManagementView.as_view(), name='get_profile'),
    path('get-profiles-list/', ProfileListAPIView.as_view(), name='get_profiles_list'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),

    path("ai/chat/", AIChatView.as_view(), name="ai-chat"),
]