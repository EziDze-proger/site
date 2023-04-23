
from django.contrib import admin
from a_eco.models import ecologiya

class ecologiyaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(ecologiya, ecologiyaAdmin)
