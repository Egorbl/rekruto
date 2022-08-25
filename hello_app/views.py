from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def hello_view(request: WSGIRequest) -> HttpResponse:
    name = request.GET.get('name') or ''
    message = request.GET.get('message') or ''
    context = {
        'name': name,
        'message': message
    }

    return render(request, 'hello_app/index.html', context)
