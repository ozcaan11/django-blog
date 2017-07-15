from django import template
from django.views.decorators.cache import cache_page

from blog.models import Tag, Setting

register = template.Library()


# @cache_page(60 * 1)
@register.inclusion_tag('blog/includes/sidebar.html')
def sidebar_tags():
    tags = Tag.objects.all()
    setting = Setting.objects.first()
    return {'tags': tags, 'setting': setting}
