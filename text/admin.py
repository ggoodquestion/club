from django.contrib import admin
from text.models import AbouTxt ,DecTxt ,ClassTxt ,Worker

class AboutAdmin(admin.ModelAdmin):
	list_display = ('txt',)

class DecAdmin(admin.ModelAdmin):
	list_display = ('title' ,'txt')

class WorkerAdmin(admin.ModelAdmin):
	list_display = ('job' ,'name')


# Register your models here.
admin.site.register(AbouTxt ,AboutAdmin)
admin.site.register(DecTxt ,DecAdmin)
admin.site.register(ClassTxt ,DecAdmin)
admin.site.register(Worker ,WorkerAdmin)