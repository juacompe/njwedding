from django.shortcuts import render_to_response
from django.template import RequestContext

def run_test(request, test_name):
    template_name = '%s.html' % test_name
    context = RequestContext(request)
    for item in context:
        for k, v in item.items():
            print '%s, %s' % (k, v)
    return render_to_response(template_name, context)

