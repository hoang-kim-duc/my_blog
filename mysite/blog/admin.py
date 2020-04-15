from django.contrib import admin
from blog.models import Comment,Post,Description, Notification
# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Notification)
admin.site.register(Description)
