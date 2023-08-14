from django import template
from blog.models import Post
from django.utils import timezone
register = template.Library()


@register.inclusion_tag('website/website-latest-from-us.html')
def latest_from_us(arg=6):
    posts = Post.objects.filter(status=1).filter(published_date__lte=timezone.now())[:arg]
    return {'posts':posts}