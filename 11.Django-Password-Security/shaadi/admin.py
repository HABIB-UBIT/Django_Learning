from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','name','age','gender','occupation','email')
    list_display_links=('name','email')
    list_filter=('gender','occupation','is_married')
    search_fields=('occupation',)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(FatherProfile)
admin.site.register(Caste)
admin.site.register(Religion)
admin.site.register(Sect)

class HobbyAdmin(admin.ModelAdmin):
    list_display=('name','get_profiles')
    def get_profiles(self,obj):
        hobby_followers=",".join([profile.name for profile in obj.profiles.all()])
        return hobby_followers
    get_profiles.short_description= "Profiles"
admin.site.register(Hobby, HobbyAdmin)