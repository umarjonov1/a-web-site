from django.http import HttpResponse
from random import randint
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request):
    obj = Article.objects.get(id=randint(1, 3))
    context = {'object': obj,
               'title': obj.title,
               'id': obj.id,
               'content': obj.content
               }
    HTML_STRING = render_to_string('home_view.html', context=context)
    return HttpResponse(HTML_STRING)