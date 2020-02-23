from django.contrib import admin

# Register your models here.
from .models import Post  # Postモデルをmodelsからimport

admin.site.register(Post)  # 管理画面でPostを登録