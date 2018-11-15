from django.shortcuts import render

from testing.tasks import digital_ocean
# Create your views here.
from transactions.models import TestInvitation


def start_project(request, id):
    digital_ocean.delay(id)
    return render(request, 'testing/start-project.html')


def call_to_apply_view(request):
    invites = TestInvitation.objects.filter(email=request.user.email)

    return render(request, 'testing/invites.html', {'invites': invites})
