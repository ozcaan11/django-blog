from django import template

from blog.models import Setting

register = template.Library()


# @cache_page(60 * 1)
@register.inclusion_tag('blog/includes/header.html')
def blog_header():
    setting = Setting.objects.first()
    return {'setting': setting}
