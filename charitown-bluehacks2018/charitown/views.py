from django.shortcuts import render
from django.views import generic
from charitown.models import Member, Community

# Create your views here.


def index(request):
    top_ten_members = Member.objects.order_by('-totalAmountDonated')[:10]
    top_ten_communities = Community.objects.order_by('totalAmountDonated')[:10]


    context = {
        'top_ten_members': top_ten_members,
        'top_ten_communities': top_ten_communities,
    }
    return render(request, 'charitown/index.html', context)


def profile(request):
    return render(request, 'charitown/view_profile.html')

def create(request):
    return render(request, 'charitown/create_account.html')

def about(request):
    return render(request, 'charitown/about.html')

def mod_community(request):
    return render(request, 'charitown/modify_community.html')

def mod_user(request):
    return render(request, 'charitown/modify_user.html')

def city(request):
    return render(request, 'charitown/view_city.html')

def search(request):
    return render(request, 'charitown/search_results.html')

def login_page(request):
    return render(request, 'charitown/login.html')

def login_attempt(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            print form.cleaned_data['my_form_field_name']

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })




# class IndexView(generic.ListView):
#     template_name = 'charitown/index.html'
#     context_object_name = 'top_members_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Member.objects.order_by('totalAmountDonated')[:10]