from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
from django.template import RequestContext
from admissions.forms import AppFormForm
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
def apply(request, institute_id, app_form_id):
    if request.method == 'GET':
        context = RequestContext(request)
        form = AppFormForm()  # An unbound form
        return render_to_response('admissions/apply_for_institution.html',
                                  {'form': form, 'institute_id': institute_id, 'app_form_id': app_form_id, }, context)
        # Refer http://jacobian.org/writing/dynamic-form-generation/
    else:  #POST
        form = AppFormForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return render_to_response('admissions/thanks.html', {}, context_instance=RequestContext(request))


@login_required
def get_applications_list(request, institute_id):
    if request.method == 'GET':
        #show list of all application forms that are published by this institute
        #institute_id = 0 # institute on which the user clicked the apply button
        return render_to_response('admissions/applications_list.html', {
            'app_form_list': AppForm.objects.filter(institute_id__institute_id__iexact=institute_id),
                'institute_id': institute_id}, context_instance=RequestContext(request))
    else:
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
def search_institutes(request):
    if request.method == 'GET':
        search_term = request.GET['q']
        if search_term:
            results = Institution.objects.filter(name__icontains=search_term)
            return render_to_response('admissions/search.html',
                                      {'search_term': search_term, 'results': results})
    else:
        pass


@login_required
def institution_details(request, institute_id):
    if request.method == 'GET':
        if institute_id and len(institute_id) > 0:
            return render_to_response('admissions/institution.html',
                                      {'institute': Institution.objects.filter(pk=institute_id)[:1]})

    else:
        pass

    pass


@login_required
def create_profile(request):
    pass


@login_required
def edit_application(request, app_id):
    # Refer here: http://stackoverflow.com/questions/13914880/auto-fill-modelform-with-data-already-stored-in-database
    ins = get_object_or_404(AppForm, appform_id=app_id)
    form = AppFormForm(instance=ins)
    if request.method == "POST":
        form = AppFormForm(request.POST, instance=ins)