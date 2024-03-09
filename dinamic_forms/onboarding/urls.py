from django.urls import include, path

from onboarding.views import onboarding_completion, success, index

app_name = 'onboarding'

urlpatterns = [
    path('', index, name='index'),
    path('form/<slug:form_tag>', onboarding_completion,
         name='onboarding_completion'),
    path('success/', success, name='success'),
]
