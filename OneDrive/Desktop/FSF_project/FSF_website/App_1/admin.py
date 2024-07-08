from django.contrib import admin
from .models import Userdata
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','number','city','regarding')
    list_display_links=('firstname',)
    list_filter=('id','firstname','city')
admin.site.register(Userdata,UserAdmin)
