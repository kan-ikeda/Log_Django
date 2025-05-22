from django import template

register = template.Library()

@register.filter(name='has_liked')
def has_liked(log, user):
    return log.likes.filter(user=user).exists()