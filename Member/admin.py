from django.contrib import admin

from .models import Member, Ministry, Shepherd

admin.site.site_header = "REVIVAL CHAPEL ADMIN"

admin.site.register(Member)
admin.site.register(Ministry)
admin.site.register(Shepherd)


