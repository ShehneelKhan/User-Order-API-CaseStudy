from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('orders/', views.OrderList.as_view(), name='orders-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('orders/by-emails/', views.OrderListByUserEmailsAPIView.as_view(), name='order-list-by-emails'),
    
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
    
]
