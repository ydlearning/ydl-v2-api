from django.contrib import admin

from .models import YDL_User, YDL_Teacher, YDL_Student

admin.site.register(YDL_User)
admin.site.register(YDL_Teacher)
admin.site.register(YDL_Student)
