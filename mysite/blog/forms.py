from django import forms
from blog.models import Post,Comment,tag_list
class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'tag', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class:':'textinputclass'}),
            'tag': forms.Select(choices=tag_list),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent border border-primary',
                                          'style':'min-height:300px;'}),
        }


class CommentForm(forms.ModelForm):
    class Meta():
      model = Comment
      fields = ('author','text')

      widgets = {
         'author':forms.TextInput(attrs={'class':'textinputclass'}),
         'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea border'}),
      }
