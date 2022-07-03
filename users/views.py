from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

class RegisterView(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']

            try:
                user = User.objects.get(username=username)
                return Response({'error': 'Username already exists'})
            except User.DoesNotExist:
                user = User()
                user.username = username
                user.email = email
                user.set_password(password)
                user.save()
                return Response({'success': 'You have successfully registered'})
        except KeyError:
            return Response({'error': 'Missing username or password'})


class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']

            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password) is True:
                    token = Token.objects.get_or_create(user=user)
                    return Response({'token': token[0].key})
                else:
                    return Response({'error': 'Invalid password'})
            except User.DoesNotExist:
                return Response({'error': 'Invalid username'})    
            
        except KeyError:
            return Response({'error': 'Missing username or password'})