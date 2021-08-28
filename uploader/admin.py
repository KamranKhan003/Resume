from django.contrib import admin
from .models import Resume

# Register Resume Model
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    
    list_display = ['id','full_name','father_name','dob', 'gender', 'city']
    radio_fields = {'gender': admin.HORIZONTAL}
