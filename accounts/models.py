from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 著者（多vs1）、１人の著者が複数の日記を書く、ondeleteは参照先が削除されたときに自分も削除
    title = models.CharField(max_length=100)  # タイトル
    text = models.TextField()  # 本文
    knowledge = models.CharField(max_length=100)  # 学んだこと
    created_date = models.DateTimeField(default=timezone.now)  # 作成日
    published_date = models.DateTimeField(blank=True)  # 投稿日

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # 特殊メゾット、関数名を呼び出さなくても実行される
        return self.title
