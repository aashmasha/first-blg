from django.contrib import admin
from .models import Post




#how to change the visible list name of model
#class PostAdmin(admin.ModelAdmin):
#	list_display=('text',)
#admin.site.register(Post,PostAdmin)

admin.site.register(Post)