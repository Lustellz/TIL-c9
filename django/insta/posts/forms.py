from django import forms
from .models import Post, Comment, Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', ]

class CommentForm(forms.ModelForm):
    content = forms.CharField(label = '', widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Comment.'}))
    
    class Meta:
        model = Comment
        fields = ['content',]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]
        
ImageFormSet = forms.inlineformset_factory(Post, Image, form=ImageForm, extra=3)