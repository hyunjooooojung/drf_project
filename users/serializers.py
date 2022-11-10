from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from articles.serializers import ArticleListSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    # followers followings 둘다 stringrelatedField로 
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    # 아니면 followers를 primarykey related로 설정
    # followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    article_set = ArticleListSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)
    
    class Meta:
        model = User
        fields = ('email', 'id', 'followings', 'followers', 'article_set', 'like_articles')
        
        
         
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        # validated_data => 패스워드, 이메일
        user = super().create(validated_data)
        # 패스워드 저장
        password = user.password
        # 저장된걸 해싱 처리
        user.set_password(password)
        # 저장된걸 db에 전달
        user.save()
        return user
    
    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token