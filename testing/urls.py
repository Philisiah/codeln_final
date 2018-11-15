from django.urls import path

from testing.views import start_project, call_to_apply_view

app_name = 'testing'

urlpatterns = [
    path('call-to-apply-view/', call_to_apply_view, name='call-to-apply-view'),
    path('start-project/<int:id>/', start_project, name='start-project'),
]
