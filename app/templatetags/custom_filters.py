from django import template

register = template.Library()

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def trim(value):
    return value.strip() if isinstance(value, str) else value



@register.filter
def is_video(file_url):
    return file_url.lower().endswith(('.mp4', '.mov', '.avi', '.mkv'))