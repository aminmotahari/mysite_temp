from django.contrib import admin


# Register your models here.
from website.models import Contact, NewsLetter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name", "subject", "email", "created_date"]
    list_filter = ["email"]
    search_fields = ["subject"]

admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsLetter)