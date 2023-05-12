from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Order
from .serializers import UserSerializer, OrderSerializer

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(
            username='admin',
            password='admin',
        )
        self.user1 = User.objects.create_user(
            username='user1@example.com',
            password='user1password',

        )
        self.user2 = User.objects.create_user(
            username='user2@example.com',
            password='user2password',

        )
        
    def test_user_list(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(reverse('users-list'))
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_user_detail(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user1.pk}))
        user = User.objects.get(pk=self.user1.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
        
        
class OrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(
            username='admin',
            password='admin',
        )
        self.user1 = User.objects.create_user(
            username='user1@example.com',
            password='user1password',
        )
        self.order1 = Order.objects.create(
            user=self.user1,
            name='Order 1',
            description='Description for order 1',
            price='10.00',
        )
        
    def test_order_list(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(reverse('orders-list'))
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_order_detail(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(reverse('order-detail', kwargs={'pk': self.order1.pk}))
        order = Order.objects.get(pk=self.order1.pk)
        serializer = OrderSerializer(order)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
        
class OrderListByUserEmailsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.user1 = User.objects.create_user(
            username='user1',
            password='testpass'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='testpass'
        )
        self.order1 = Order.objects.create(
            user=self.user1,
            name='Order 1',
            description='Description 1',
            price=10.0
        )
        self.order2 = Order.objects.create(
            user=self.user2,
            name='Order 2',
            description='Description 2',
            price=20.0
        )

    def test_list_orders_by_user_emails_unauthenticated(self):
        url = reverse('order-list-by-emails')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_orders_by_user_emails_authenticated_user(self):
        url = reverse('order-list-by-emails')
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

