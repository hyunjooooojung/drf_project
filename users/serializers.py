from rest_framework import serializers
from users.models import User


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