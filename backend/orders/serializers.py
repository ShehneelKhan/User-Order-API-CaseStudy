from rest_framework import serializers
from .models import User, Order
from rest_framework.serializers import CurrentUserDefault


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
            }
        
        
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'user_id', 'name', 'description', 'price', 'created_at', 'updated_at']
    
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        
        if password!= confirm_password:
            raise serializers.ValidationError({'error': 'Passwords do not match'})

        if User.objects.filter(email=self.validated_data['email']):
            raise serializers.ValidationError({'error': 'Email already in use'})
                  
                  
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
        