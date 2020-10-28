from django import template

register = template.Library()

# Custom template filter

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
# Since we are passing a funciton into another, we can use decorators instead of the above line
