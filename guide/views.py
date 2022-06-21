from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def index(req):
    subject_name = SubjectInfo.objects.order_by('name')
    context = {
        'subject': subject_name
    }
    return render(req, 'index.html', context=context)


class CodeView(ListView):
    model = Code
    context_object_name = 'code_list'
    template_name = 'codes/codelist.html'
    queryset = Code.objects.order_by('name').all()


class CodeDetail(DetailView):
    model = Code
    context_object_name = 'code_detail'
    template_name = 'codes/code.html'


class SitView(ListView):
    model = Sit
    context_object_name = 'sit_list'
    template_name = 'codes/sitlist.html'
    queryset = Sit.objects.order_by('name').all()


class SitDetail(DetailView):
    model = Sit
    context_object_name = 'sit_detail'
    template_name = 'codes/sit.html'


