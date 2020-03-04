from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from weasyprint import HTML

from .models import RunoDB

# Create your views here. Changed to use class based views 2020-03- 05. function based in RunoFuncs -Scratch file


class RunoList(ListView):
    model = RunoDB


class RunoRead(DetailView):
    model = RunoDB


class RunoCreate(CreateView):
    model = RunoDB
    fields = ['name',
              'caption',
              'author'
              ]


class RunoEdit(UpdateView):
    model = RunoDB
    fields = ['name',
              'caption',
              'author',
              'picture',
              'rate'
              ]
    template_name_suffix = '_update_form'


class RunoDelete(DeleteView):
    model = RunoDB
    success_url = reverse_lazy('runolista')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def html_to_pdf_view(request, *args):
    paragraphs = RunoDB.objects.filter(*args)
    html_string = render_to_string('runoApp/pdf_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/parhaat_runot.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('parhaat_runot.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="parhaat_runot.pdf"'
        return response

    return response


def html_to_pdf_one_view(request, pk):
    paragraphs = RunoDB.objects.filter(pk=pk)
    html_string = render_to_string('runoApp/pdf_template.html', {'paragraphs': paragraphs})
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/runo.pdf')

    fs = FileSystemStorage('/tmp')

    with fs.open('runo.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="runo.pdf"'
        return response

    return response
