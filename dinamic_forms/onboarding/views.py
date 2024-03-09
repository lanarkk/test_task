from django.shortcuts import get_object_or_404, render

from django.urls import reverse_lazy
from onboarding.models import TemplateField, Template, Record, RecordData
from onboarding.forms import CDBForm

from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


def success(request):
    template = 'onboarding/success.html'
    return render(request, template)


def index(request):
    instance = Template.objects.all()
    context = {'page_obj': instance}
    return render(request, 'onboarding/index.html', context)


def onboarding_completion(request, form_tag):
    template = get_object_or_404(Template, tag=form_tag)
    form = CDBForm(template=template, tag=form_tag)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'onboarding/forms.html', context)
