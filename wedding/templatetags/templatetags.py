import markdown
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))