from django.contrib import admin
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from blog.models import Post, Category
#Post.objects.filter(published_date__lte=timezone.now())
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["title", "author", "counted_view", "status", "published_date", "created_date"]
    list_filter = ["status", "author"]
    search_fields = ["title"]
    # ordering = ["created_date"]
    summernote_fields = ('content',)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
