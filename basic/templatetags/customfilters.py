from django import template
from num2words import num2words

register = template.Library()

def first_five_upper(value):
    result = value[:5].upper()
    return result

def first_n_upper(value, n):
    result = value[:n].upper()
    return result

def length_limit(value, limit):
    if len(value) > limit:
        return value[0:limit] + '...'
    else:
        return value
    
def rating(value):
    if(float(value) >= 4):
        return value + '[Excellent]'
    if(float(value) >= 3):
        return value + '[Very good]'
    if(float(value) >= 1.5):
        return value + '[Average]'
    else:
        return value + '[Poor]'

def convertnumbertowords(value):
    return num2words(value)

register.filter('firstfiveupper', first_five_upper)
register.filter('firstnupper', first_n_upper)
register.filter('lengthlimit', length_limit)
register.filter('rating', rating)
register.filter('convertnumbertowords', convertnumbertowords)