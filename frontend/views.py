from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from accounts.forms import ProfileTypeForm, DeveloperFillingDetailsForm, RecruiterFillingDetailsForm
from projects.models import Project, OngoingProjects
from transactions.models import Transaction, Candidate


@login_required
def developer_filling_details(request, current_profile):
    if request.method == 'POST':
        developer_filling_details_form = DeveloperFillingDetailsForm(request.POST, request.FILES)
        if developer_filling_details_form.is_valid():
            current_profile.profile_photo = developer_filling_details_form.cleaned_data['profile_photo']
            current_profile.github_repo = developer_filling_details_form.cleaned_data['github_repo']
            current_profile.language = developer_filling_details_form.cleaned_data['language']
            current_profile.framework = developer_filling_details_form.cleaned_data['framework']
            current_profile.years = developer_filling_details_form.cleaned_data['years']
            current_profile.stage = 'complete'
            current_profile.save()
            return redirect(reverse('frontend:index'))
    else:
        developer_filling_details_form = DeveloperFillingDetailsForm()
    return render(request, 'frontend/developer/developer_filling_details.html',
                  {'developer_filling_details_form': developer_filling_details_form})


@login_required
def recruiter_filling_details(request, current_profile):
    if request.method == 'POST':
        recruiter_filling_details_form = RecruiterFillingDetailsForm(request.POST)
        if recruiter_filling_details_form.is_valid():
            current_profile.company = recruiter_filling_details_form.cleaned_data['company']
            current_profile.job_role = recruiter_filling_details_form.cleaned_data['job_role']
            current_profile.industry = recruiter_filling_details_form.cleaned_data['industry']
            current_profile.staff_size = recruiter_filling_details_form.cleaned_data['staff_size']
            current_profile.company_url = recruiter_filling_details_form.cleaned_data['company_url']
            current_profile.stage = 'complete'
            current_profile.save()
            return redirect(reverse('frontend:index'))
    else:
        recruiter_filling_details_form = RecruiterFillingDetailsForm()
    return render(request, 'frontend/recruiter/recruiter_filling_details.html',
                  {'recruiter_filling_details_form': recruiter_filling_details_form})


@login_required
def profile_type_selection(request, current_profile):
    if request.method == 'POST':
        profile_type_form = ProfileTypeForm(request.POST)
        if profile_type_form.is_valid():
            profile_type = profile_type_form.cleaned_data['profile_type']
            current_profile.user_type = profile_type
            if profile_type == 'developer':
                current_profile.stage = 'developer_filling_details'
            elif profile_type == 'recruiter':
                current_profile.stage = 'recruiter_filling_details'
            current_profile.save()
            return redirect(reverse('frontend:index'))
    else:
        profile_type_form = ProfileTypeForm()
    return render(request, 'frontend/profile_type_selection.html', {'profile_type_form': profile_type_form})


def index(request):
    if request.user.is_authenticated:
        current_profile = request.user.profile
        if request.user.profile.stage == 'developer_filling_details':
            return developer_filling_details(request, current_profile)

        elif request.user.profile.stage == 'recruiter_filling_details':
            return recruiter_filling_details(request, current_profile)

        elif request.user.profile.stage == 'complete':
            if request.user.profile.user_type == 'developer':
                return render(request, 'frontend/developer/developer.html')
            
            elif request.user.profile.user_type == 'recruiter':
                return render(request, 'frontend/recruiter/recruiter.html')
    else:
        return home(request)


def home(request):
    return render(request, 'frontend/landing.html')


@login_required
def activity(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user)
        if request.user.profile.user_type == 'recruiter':
            return render(request, 'frontend/recruiter/my-activity.html', {'transactions': transactions})
        elif request.user.profile.user_type == 'developer':
            return render(request, 'frontend/developer/my-activity.html', {'transactions': transactions})


def tracker(request, id):
    candidates = Candidate.objects.filter(transaction_id=id)
    return render(request, 'frontend/recruiter/tracker.html', {'candidates': candidates})


def inprogress(request):
    global ongoing_projects
    candidates = Candidate.objects.filter(email=request.user.email)
    if request.user.profile.user_type == 'developer':
        ongoing_projects = OngoingProjects.objects.filter(candidate=request.user)
    elif request.user.profile.user_type == 'recruiter':
        ongoing_projects = OngoingProjects.objects.filter(assigner=request.user)
    return render(request, 'frontend/developer/inprogress.html',
                  {'candidates': candidates, 'ongoing_projects': ongoing_projects})


def invites(request):
    candidates = Candidate.objects.filter(email=request.user.email)
    return render(request, 'frontend/developer/invites.html', {'candidates': candidates})


def projectdetails(request, id):
    project = Project.objects.get(id=id)

    return render(request, 'frontend/developer/projectdetails.html', {'project': project})


def pendingproject(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'frontend/developer/pendingproject.html', {'project': project})


def pricing(request):
    return render(request, 'frontend/pricing.html')


def dev(request):
    return render(request, 'frontend/dev.html')


def howitworks(request):
    return render(request, 'frontend/how.html')


def report(request, email, transaction_id):
    user = User.objects.get(email=email)
    transaction = Transaction.objects.get(id=transaction_id)

    return render(request, 'frontend/recruiter/report.html', {'user': user, 'transaction': transaction})


def credits(request):
    return render(request, 'frontend/credits.html')


def privacy(request):
    return render(request, 'frontend/privacy.html')


def terms(request):
    return render(request, 'frontend/terms.html')


def sample(request):
    return render(request, 'frontend/sample.html')


def page_404(request):
    return render(request, 'frontend/error_pages/404.html')


def page_500(request):
    return render(request, 'frontend/error_pages/500.html')


def samplereport(request):
    return render(request, 'frontend/recruiter/samplereport.html')
