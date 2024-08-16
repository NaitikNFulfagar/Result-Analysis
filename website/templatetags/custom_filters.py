# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def initials(value):
    if not isinstance(value, str):
        return value
    words = value.split()
    if len(words) == 1:
        return value  # Return the whole word if it's a single word
    return ''.join([word[0] for word in words])



@register.filter(name='split_and_join')
def split_and_join(value, arg):
    return "\n".join(value.split(arg))


# def initials(value):
#     if not isinstance(value, str):
#         return value
#     return ''.join([word[0] for word in value.split()])
