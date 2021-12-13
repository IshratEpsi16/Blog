from django import template
register = template.Library()
def range_filter(value):
    return value[0:200] + '.........'
register.filter('range_fiter',range_filter)