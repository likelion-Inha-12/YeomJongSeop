from django.db import models


class Member(models.Model):

    name = models.CharField(max_length=20)  # 이름은 20자로 제한
    email = models.EmailField(unique=True)  # 이메일 필드는 고유해야 함

    def __str__(self):
        return self.name
    

class Post(models.Model):

    title = models.CharField(max_length=50)  # 제목은 50자로 제한
    content = models.TextField(null=True, blank=True)  # 본문은 글자 수 제한 없음, null과 blank 허용
    create_at = models.DateTimeField(auto_now_add=True)  # 생성 시간 자동 기록
    author = models.ForeignKey(Member,on_delete=models.CASCADE,null=True)  # 글 작성자(Member의 id를 FK로 사용) null=True 안붙이면 오류!!
    member_id = models.ForeignKey(Member, verbose_name="Member", on_delete=models.CASCADE, related_name="posts", null=True) #null=True 안붙이면 오류!!

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.CharField(max_length = 200, null = True, blank = True)
    member_id = models.ForeignKey(Member, verbose_name="Member", on_delete=models.CASCADE, related_name="comments", null=True)  # 댓글 작성자
    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name="comments") #연관 포스트

    def __str__(self):  
        return self.content
    
class UserPost(models.Model):
    user_id = models.ForeignKey(Member, verbose_name="user", on_delete=models.CASCADE, related_name='liked_posts')  # '좋아요'를 누른 사용자
    post_id = models.ForeignKey(Post, verbose_name="post", on_delete=models.CASCADE, related_name='likers')  # '좋아요'를 받은 포스트

    class UserPost:
        unique_together = ('user_id', 'post_id')  # 유저와 포스트의 조합은 유니크해야 함

    def __str__(self):
        return f"{self.user_id.name} likes {self.post_id.title}"