from django.contrib import admin
from hr.models import contact
from hr.models import task, leave

# Register your models here.
admin.site.register(contact)
admin.site.register(task)
admin.site.register(leave)