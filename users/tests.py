from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User



class UserRegistrationTest(APITestCase):
    def test_registration(self):
        # 장고에서 알아서 name에 해당되는 url을 가져온다.
        url = reverse('user_view')
        user_data = {
            "email": "hyun@naver.com",
            "password": "1234",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201)
        
class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {'email':'hyun@naver.com', 'password':'1234'}
        self.user = User.objects.create_user('hyun@naver.com', '1234')
    
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code, 200)
        
    def test_get_user_data(self):
        access_token = self.client.post(reverse('token_obtain_pair'),self.data).data['access']
        response = self.client.get(
            path=reverse('user_view'),
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        self.assertEqual(response.status_code, 405)
        # self.assertEqual(response.data['username'], self.data['username'])