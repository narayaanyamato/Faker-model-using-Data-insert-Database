from django.contrib import admin
from modelapp3.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['sno','sname','sroll','email','dob','mark','phone','address']
admin.site.register(Student,StudentAdmin)    
