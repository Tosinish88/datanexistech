from django.contrib import admin
from .models import ContactMessage
from .models import Service, ServiceTitle, Team
# Register your models here.

class ServiceTitleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # list_display = ('instructor','course_title', 'created_at', )
    # list_display_links = ('instructor', 'course_id',)

admin.site.register(Service)
admin.site.register(Team)
admin.site.register(ServiceTitle, ServiceTitleAdmin)
admin.site.register(ContactMessage)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'created_at')
    search_fields = ('firstname', 'lastname', 'email', 'message')