from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post,Comment,Notification,Description
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                  UpdateView, DeleteView)

# Create your views here.

class ListView(ListView):
   def get_context_data(self, **kwargs):
        ctx = super(ListView, self).get_context_data(**kwargs)
        ctx['Notification'] = Notification.objects.order_by('-time')
        return ctx


class DetailView(DetailView):
   def get_context_data(self, **kwargs):
        ctx = super(DetailView, self).get_context_data(**kwargs)
        ctx['Notification'] = Notification.objects.order_by('-time')
        return ctx
   


class TemplateView(TemplateView):
   def get_context_data(self, **kwargs):
        ctx = super(TemplateView, self).get_context_data(**kwargs)
        ctx['Notification'] = Notification.objects.all()
        return ctx


class AboutView(TemplateView):
   template_name = 'blog/about.html'

class PostListView(ListView):
   context_object_name = 'post_list'
   model = Post

   def get_queryset(self):
      return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
   
   def get_context_data(self, **kwargs):
      ctx = super(ListView, self).get_context_data(**kwargs)
      ctx['Description'] = Description.objects.get(pk=4)
      ctx['Notification'] = Notification.objects.order_by('-time')
      return ctx


class Tag1ListView(ListView):
   model = Post
   def get_queryset(self):
      return Post.objects.filter(published_date__lte=timezone.now(),tag='tag1').order_by('-published_date')

   def get_context_data(self, **kwargs):
      ctx = super(ListView, self).get_context_data(**kwargs)
      ctx['Description'] = Description.objects.get(pk=1)
      ctx['Notification'] = Notification.objects.order_by('-time')
      return ctx


class Tag2ListView(ListView):
   model = Post

   def get_queryset(self):
      return Post.objects.filter(published_date__lte=timezone.now(), tag='tag2').order_by('-published_date')

   def get_context_data(self, **kwargs):
      ctx = super(ListView, self).get_context_data(**kwargs)
      ctx['Description'] = Description.objects.get(pk=2)
      ctx['Notification'] = Notification.objects.order_by('-time')
      return ctx


class Tag3ListView(ListView):
   model = Post

   def get_queryset(self):
      return Post.objects.filter(published_date__lte=timezone.now(), tag='tag3').order_by('-published_date')

   def get_context_data(self, **kwargs):
      ctx = super(ListView, self).get_context_data(**kwargs)
      ctx['Description'] = Description.objects.get(pk=3)
      ctx['Notification'] = Notification.objects.order_by('-time')
      return ctx


class PostDetailView(DetailView):
   context_object_name = 'post_detail'
   model = Post


   def get_object(self):
      post = super().get_object()
      if not self.request.user.is_authenticated:
         post.increase_view()
      return post
      

class CreatePostView(LoginRequiredMixin,CreateView):
   login_url = 'login/'
   redirect_field_name = 'blog/post_detail.html'
   form_class = PostForm
   model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
   login_url = 'login/'
   redirect_field_name = 'blog/post_detail.html'
   form_class = PostForm
   model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
   model = Post
   success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
   login_url = 'login/'
   redirect_field_name = 'blog/post_list.html'
   model = Post
   context_object_name = 'post_list'

   def get_queryset(self):
      return Post.objects.filter(published_date__isnull=True).order_by('-create_date')



################################
################################

@login_required
def post_publish(request,pk):
   post = get_object_or_404(Post,pk=pk)
   post.publish()
   return redirect('post_detail',pk=pk)


def add_comment_to_post(request,pk):
   post = get_object_or_404(Post,pk=pk)
   if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save() 
            notification = Notification()
            notification.person = comment.author
            notification.action = 'đã thêm một bình luận ở bài viết'
            notification.post_title = '\"' + post.title + '\"'
            notification.target = 'post'
            notification.id_target = post.pk
            notification.save()
            return redirect('post_detail',pk=post.pk)
   else:
      form = CommentForm()
   return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
   comment = get_object_or_404(Comment,pk=pk)
   comment.approve()
   return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
   comment = get_object_or_404(Comment,pk=pk)
   post_pk = comment.post.pk
   comment.delete()
   return redirect('post_detail',pk=post_pk)
