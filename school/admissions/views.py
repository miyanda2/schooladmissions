from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext
from admissions.models import Institution, AppForm


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


@login_required
def apply(request):
    pass


# Clicking on the Apply button brings user to the list of institutions that have application forms posted.
# User can pick one of the institutions and apply.
@login_required
def institution_list(request):
    if request.method == 'GET':
        return render_to_response('admissions/institution_list.html', {'institute_list': Institution.objects.all()})

    else:
        pass

    pass


@login_required
def institution_details(request, institute_id):
    if request.method == 'GET':
        if institute_id and len(institute_id) > 0:
            return render_to_response('admissions/institution.html', {'institute': Institution.objects.filter(pk=institute_id)[:1]})

    else:
        pass

    pass


@login_required
def create_profile(request):
    pass