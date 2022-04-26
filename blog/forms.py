from django import forms

from .models import Post, Servey, Servey_re, Tag, YesOrNo, ThreeChoices, ThreeChoices_re

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'tag', 'text', 'voice_first', 'voice_second', 'voice_third', 'place', 'screenshot', 'maps')
        
class Servey_reForm(forms.ModelForm):
    class Meta:
        model = Servey_re
        fields = ('question_already', 'question_understanding', 'question_suitable','question_changes','question_reasons','question_requests')
        widgets = {
            'question_already': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'question_understanding': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'question_suitable': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'question_changes': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
        }


                
#class ServeyForm(forms.ModelForm):	
#	class Meta:
#		model = Servey
#        fields = ('student_number', 'question')
#        widgets = {
#            'needs': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
#        }
        