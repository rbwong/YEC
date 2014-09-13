from django.contrib import admin
from .models import Make


class MakeAdmin(admin.ModelAdmin):
    list_display = ('first_name1',
                    'middle_name1',
                    'last_name1',
                    'email1',
                    'phone1',
                    'sid1',
                    'school1',
                    'year_level1',
                    'course1',
                    'id_pic1',
                    'first_name2',
                    'middle_name2',
                    'last_name2',
                    'email2',
                    'phone2',
                    'sid2',
                    'year_level2',
                    'course2',
                    'id_pic2',
                    'app_name',
                    'purpose',
                    'app_market',
                    'concept',)

admin.site.register(Make, MakeAdmin)
