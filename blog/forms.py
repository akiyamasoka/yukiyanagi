from django import forms

from .models import Post, Servey, Tag

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'tag', 'text')
        
class ServeyForm(forms.ModelForm):
	
	class Meta:
		model = Servey
		fields = ('student_number', 'needs', 'question')
		widgets = {
            'tag': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
        }
		