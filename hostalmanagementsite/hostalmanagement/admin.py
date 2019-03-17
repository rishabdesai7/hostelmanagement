from django.contrib import admin
import hostalmanagement.models as m
# Register your models here.
admin.site.register(m.hostel)
admin.site.register(m.users)
admin.site.register(m.applications)
admin.site.register(m.complaint)
admin.site.register(m.rooms)


