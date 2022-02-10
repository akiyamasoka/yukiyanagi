from django.contrib import admin
from .models import Post, Servey, Tag, Maps

class ServeyAdmin(admin.ModelAdmin):
	list_display = ('student_number','_needs','question','institution','published_date')
	ordering = ('-institution',)
	list_filter = ('needs',)
	search_fields = ('student_number', 'question', 'institution')
	
	def _needs(self, row):
		return ','.join([x.name for x in row.needs.all()])
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'text', 'voice_first', 'voice_second', 'voice_third', 'place', 'screenshot', '_maps')
    
    def _maps(self, row):
        return ','.join([x.name for x in row.needs.all()])
    

admin.site.register(Post, PostAdmin)
admin.site.register(Servey, ServeyAdmin)
admin.site.register(Tag)
admin.site.register(Maps)
