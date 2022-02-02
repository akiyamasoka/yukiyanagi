from django.contrib import admin
from .models import Post, Servey, Tag

class ServeyAdmin(admin.ModelAdmin):
	list_display = ('student_number','needs','question','institution','published_date')
	ordering = ('-institution',)
	list_filter = ('needs',)
	search_fields = ('student_number', 'question', 'institution')

admin.site.register(Post)
admin.site.register(Servey, ServeyAdmin)
admin.site.register(Tag)
