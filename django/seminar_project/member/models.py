from django.db import models

class Member(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # id 필드를 문자열로 선언하고, 기본 키로 설정합니다.
    email = models.EmailField()  # 이메일 필드
    is_leader = models.BooleanField(default=False)  # 팀 리더 여부, 기본값은 False
    hearts = models.IntegerField()  # 하트 수, 정수 필드

    def toggle_leader(self):
        self.is_leader = not self.is_leader
        self.save()

