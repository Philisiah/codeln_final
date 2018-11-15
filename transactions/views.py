from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from projects.models import Project, RecruiterProject, Language, Framework
from transactions.forms import CandidateForm, SourcingForm, StackForm
from transactions.models import Transaction, Candidate, TestInvitation


# payments view


# Create your views here.
def transaction_view(request, id):
    if request.method == 'POST':
        stack_form = StackForm(request.POST)
        if stack_form.is_valid():
            project = Project.objects.get(id=id)
            recruiter_project, created = RecruiterProject.objects.get_or_create(recruiter=request.user,
                                                                                project=project,
                                                                                language=Language.objects.get(
                                                                                    name=stack_form.cleaned_data[
                                                                                        'language']),
                                                                                framework=Framework.objects.get(
                                                                                    name=stack_form.cleaned_data[
                                                                                        'framework']))
            new_transaction = Transaction.objects.create(user=request.user, recruiter_project=recruiter_project,
                                                         stage='upload-candidates')
            return redirect(reverse('transactions:process_transaction', args=(new_transaction.id,)))
    else:
        return HttpResponse('Ok')


def process_transaction(request, id):
    current_transaction = Transaction.objects.get(id=id)
    if current_transaction.stage == 'upload-candidates':
        return upload_candidates(request, current_transaction)
    elif current_transaction.stage == 'payment-stage':
        return all_candidates(request, current_transaction)
    elif current_transaction.stage == 'payment-verified':
        return invitations(request, current_transaction)
    elif current_transaction.stage == 'complete':
        # return redirect(reverse('frontend:index'))
        return invitations(request, current_transaction)


def upload_candidates(request, current_transaction):
    # id is transaction id
    # TODO: add capapility to upload text document or csv file of Candidates
    if request.method == 'POST':
        candidate_form = CandidateForm(request.POST)
        if request.POST.get('and_continue'):
            if candidate_form.is_valid():
                current_transaction.stage = 'payment-stage'
                first_name = candidate_form.cleaned_data['first_name']
                last_name = candidate_form.cleaned_data['last_name']
                email = candidate_form.cleaned_data['email']
                new_candidate = Candidate.objects.create(first_name=first_name, last_name=last_name, email=email,
                                                         transaction=current_transaction)
                new_candidate.save()
                current_transaction.save()
                return redirect(reverse('transactions:process_transaction', args=[current_transaction.id]))

        elif request.POST.get("add_another"):
            if candidate_form.is_valid():
                current_transaction.stage = 'upload-candidates'
                first_name = candidate_form.cleaned_data['first_name']
                last_name = candidate_form.cleaned_data['last_name']
                email = candidate_form.cleaned_data['email']
                new_candidate = Candidate.objects.create(first_name=first_name, last_name=last_name, email=email,
                                                         transaction=current_transaction)
                new_candidate.save()
                return redirect(reverse('transactions:process_transaction', args=[current_transaction.id]))
        else:
            candidate_form = CandidateForm()
            return render(request, 'transactions/upload_candidate.html',
                          {'candidate_form': candidate_form, 'current_transaction': current_transaction})

    else:
        candidate_form = CandidateForm()
        return render(request, 'transactions/upload_candidate.html',
                      {'candidate_form': candidate_form, 'current_transaction': current_transaction})


def all_candidates(request, current_transaction):
    candidates = Candidate.objects.filter(transaction=current_transaction)
    total_amount = current_transaction.amount()
    return render(request, 'transactions/process_transaction.html',
                  {'candidates': candidates,
                   'total_amount': total_amount,
                   'current_transaction': current_transaction
                   })


def invitations(request, current_transaction):
    candidates = Candidate.objects.filter(transaction=current_transaction)
    if candidates.count() != 0:
        for candidate in candidates:
            TestInvitation.objects.create(email=candidate.email,
                                          recruiter_project=current_transaction.recruiter_project)
            # if candidate.email in [user.email for user in User.objects.all()]:
            #     pass
            #     # send notification
            # else:
            #     # send email telling them to signup and accept invitation
            #     # Consideration: if the user isn't a user already, should an OngoingProject be created for the user?
            #     # That is Invitation accepted automatically
            #     invite = Invitation.create(candidate.email, inviter=request.user)
            #     invite.send_invitation(request)
        current_transaction.stage = 'complete'
        current_transaction.save()
    return render(request, 'transactions/invitations.html',
                  {'candidates': candidates, 'current_transaction': current_transaction})


def my_invites(request):
    candidates = Candidate.objects.filter(email=request.user.email)
    return render(request, 'transactions/send_credentials.html', {'candidates': candidates})


def sourcing(request):
    if request.method == 'POST':
        form = SourcingForm(request.POST)
        if form.is_valid():
            subject = 'Sourcing Request'
            from_email = form.cleaned_data['email_address']
            data = ""
            data += form.cleaned_data['name']
            data += str(form.cleaned_data['phone_number'])
            data += form.cleaned_data['company_name']
            data += str(form.cleaned_data['job_role'])
            data += form.cleaned_data['engagement_types']
            data += form.cleaned_data['tech_stack']
            data += form.cleaned_data['project_description']
            data += str(form.cleaned_data['devs_needed'])
            data += str(form.cleaned_data['renumeration'])
            data += form.cleaned_data['tech_staff']
            data += form.cleaned_data['skills_test']
            try:
                send_mail(subject, data, from_email, ['philisiah@codeln.com'])
            except BadHeaderError:
                print('invalid error')
            return redirect('frontend:home')
    else:
        form = SourcingForm()
        return render(request, 'transactions/sourcing.html', {'form': form})
