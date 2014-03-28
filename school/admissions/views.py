from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext
from admissions.models import Institution


def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of all institutions currently stored.
    # Retrieve the top 5 only. Place the list in our context_dict dictionary which will be passed to the template engine.
    institution_list = Institution.objects.order_by('name')[:5]
    context_dict = {'institutions': institution_list}

    # Render the response and send it back!
    return render_to_response('index.html', context_dict, context)


def about(request):
    # Render the response and send it back!
    context = RequestContext(request)
    return render_to_response('about.html', {}, context)


