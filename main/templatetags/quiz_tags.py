from django import template

from main.models import *

register = template.Library()


@register.filter
def get_answers(question):
    res = question.quizanswer_set.all()
    return res
