from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    likes = models.ManyToManyField(User, through='Like', through_fields=('blog', 'user'), related_name="likes")
    
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #추가코드
    def __str__(self):
        return self.title


    
class Comment(models.Model):                                         #추가코드 : 댓글 create 기능
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField('data published')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)       #댓글 작성자 선택
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)         #블로그의 글 하나를 연결시킴

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


