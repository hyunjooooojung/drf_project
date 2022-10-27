from rest_framework import serializers

from articles.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    # user의 값을 email로 받아오는 것으로 변경
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article',)
    
     
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)
        

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    # comment는 Foreign key로 받아오고 있기 때문에 역참조 set 사용! or related_name 설정했기 때문에 comments로 받아옴
    comments = CommentSerializer(many=True) 
    # 좋아요 눌렀을 때 누른 사람 username이 나오도록 변경
    likes = serializers.StringRelatedField(many=True)
    
    # user의 값을 email로 받아오는 것으로 변경
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'image', 'content')
        
        
class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    
    
    # user의 값을 email로 받아오는 것으로 변경
    def get_user(self, obj):
        return obj.user.email
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()
    
    class Meta:
        model = Article
        fields = ('pk', 'title', 'image', 'updated_at', 'user', 'likes_count', 'comments_count')