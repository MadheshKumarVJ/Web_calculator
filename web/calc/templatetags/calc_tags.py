from django import template
from ..forms import Calculator

register = template.Library()


@register.simple_tag
def sum(num1, num2):
    result = num1 + num2
    return result


@register.simple_tag
def sub(num1, num2):
    result = num1 - num2
    return result


@register.simple_tag
def mul(num1, num2):
    result = num1 * num2
    return result


@register.simple_tag
def div(num1, num2):
    result = num1 / num2
    return result
