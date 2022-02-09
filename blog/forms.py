from django import forms

from .models import Post, Servey, Tag

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'tag', 'text', 'voice_first', 'voice_second', 'voice_third', 'place', 'screenshot', 'maps')
        
class ServeyForm(forms.ModelForm):
	
	class Meta:
		model = Servey
		fields = ('student_number', 'needs', 'question')
		widgets = {
            'needs': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
        }
        