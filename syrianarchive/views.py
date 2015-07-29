from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render



def handler404(request):
    response = render(request, '404.html')
    response.status_code = 400
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response