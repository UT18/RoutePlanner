from django.http import HttpResponse
from django.template import loader


def example(request):
    template = loader.get_template('example.html')
    context = {'data': 123}
    return HttpResponse(template.render(context, request))