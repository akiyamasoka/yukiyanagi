from django.contrib import admin
from .models import Post, Servey, Tag, YesOrNo, ThreeChoices, ThreeChoices_re

class ServeyAdmin(admin.ModelAdmin):
	#list_display = ('student_number','_needs','question','institution','published_date')
    list_display = ('_question_alreadys','_question_understandings','_question_suitables','_question_changess','question_reasons','question_requests','institution','published_date')
	ordering = ('-institution',)
	#list_filter = ('needs',)
	#search_fields = ('student_number', 'question', 'institution')
	
	#def _needs(self, row):
		#return ','.join([x.name for x in row.needs.all()])
        def _question_alreadys(self, row):
        return ','.join([x.name for x in row.needs.all()])
    def _question_understandings(self, row):
        return ','.join([x.name for x in row.needs.all()])
    def _question_suitables(self, row):
        return ','.join([x.name for x in row.needs.all()])
    def _question_changess(self, row):
        return ','.join([x.name for x in row.needs.all()])
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'text', 'voice_first', 'voice_second', 'voice_third', 'place', 'screenshot', 'maps')
    

admin.site.register(Post, PostAdmin)
admin.site.register(Servey, ServeyAdmin)
admin.site.register(Tag)
admin.site.register(YesOrNo)
admin.site.register(ThreeChoices)
admin.site.register(ThreeChoices_re)

