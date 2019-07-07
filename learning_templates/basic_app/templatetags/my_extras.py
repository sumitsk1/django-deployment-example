from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):# hare the value is the key value from the dict and arg is that what you want to replace  
    """
        this cuts all value of args from string
    """
    return value.replace(arg,'') # from value , arg value will be replcedm with the '' empty string