from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
tag_list = (('tag1','Kinh nghiệm học tập'),
            ('tag2','Chủ đề công nghệ'),
            ('tag3','Linh tinh cá nhân'),)
class Post(models.Model):
   author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   text = models.TextField()
   create_date = models.DateTimeField(default=timezone.now)
   published_date = models.DateTimeField(blank=True,null=True)
   tag = models.CharField(choices=tag_list, max_length=20, default='tag1')
   view = models.IntegerField(default=0)

   def increase_view(self):
      self.view = self.view + 1
      self.save()

   def publish(self):
      self.published_date = timezone.now()
      self.save()

   # def increase_view(self):


   def approve_comments(self):
      return self.comments.filter(approved_comment=True)

   def get_absolute_url(self):
      return reverse("post_detail",kwargs={'pk':self.pk})

   def __str__(self):
      return self.title


class Comment(models.Model):
   post = models.ForeignKey(
      'blog.Post', related_name='comments', on_delete=models.CASCADE)
   author = models.CharField(max_length=200)
   text = models.TextField()
   create_date = models.DateTimeField(default=timezone.now)
   approved_comment = models.BooleanField(default=False)

   def approve(self):
      self.approved_comment=True
      self.save()

   def get_absolute_url(self):
      return reverse('post_list')

   def __str__(self):
      return self.text


class Event(models.Model):
   title = models.CharField(max_length=200)
   text = models.TextField()
   occur_date = models.DateTimeField(default=timezone.now)
   create_date = models.DateTimeField(default=timezone.now)
   published_date = models.DateTimeField(blank=True, null=True)

   def __str__(self):
      return self.title

class Notification(models.Model):
   person = models.CharField(max_length=200)
   action = models.CharField(max_length=200)
   post_title = models.CharField(max_length=200)
   target = models.CharField(max_length=200)
   id_target = models.IntegerField()
   time = models.DateTimeField(default=timezone.now)
   is_read = models.BooleanField(default=False)
   
   def __str__(self):
      template = f'{self.person} {self.action} {self.post_title}'
      return template


class Description(models.Model):
   text = models.TextField()

   def __str__(self):
      return self.id
