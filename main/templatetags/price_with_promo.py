from django import template

from main.models import *

register = template.Library()


@register.filter
def price_with_promo(price, user):
    person = user.person_set.get()
    if person.discount == 0:
        return price
    else:
        new_price = round(price - price * person.discount / 100, 2)
        return new_price



