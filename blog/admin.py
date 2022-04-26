from django.contrib import admin
from .models import Post, Servey, Servey_re, Tag, YesOrNo, TwoChoices, ThreeChoices, ThreeChoices_re

#class ServeyAdmin(admin.ModelAdmin):
	#list_display = ('student_number','_needs','question','institution','published_date')
	#ordering = ('-institution',)
	#list_filter = ('needs',)
	#search_fields = ('student_number', 'question', 'institution')
	
	#def _needs(self, row):
	#	return ','.join([x.name for x in row.needs.all()])

    
class Servey_reAdmin(admin.ModelAdmin):
    list_display = ('_question_already','_question_understanding','_question_suitable','_question_changes','question_reasons','question_requests','institution','published_date')
    ordering = ('-institution',)

    def _question_already(self, row):
        return ','.join([x.name for x in row.needs.all()])
    def _question_understanding(self, row):
        return ','.join([x.name for x in row.needs.all()])
    def _question_suitable(self, row):
        return ','.join([x.name for x in row.needs.all()])
    def _question_changes(self, row):
        return ','.join([x.name for x in row.needs.all()])
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'text', 'voice_first', 'voice_second', 'voice_third', 'place', 'screenshot', 'maps')
    

admin.site.register(Post, PostAdmin)
#admin.site.register(Servey, ServeyAdmin)
admin.site.register(Servey_re,Servey_reAdmin)
admin.site.register(Tag)
admin.site.register(YesOrNo)
admin.site.register(TwoChoices)
admin.site.register(ThreeChoices)
admin.site.register(ThreeChoices_re)

