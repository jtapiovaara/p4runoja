from django.shortcuts import render
from .models import RunoDB
from django.shortcuts import render, redirect
from .forms import RunoForm
# from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

# Create your views here.


def runoLista(request):
    shelf = RunoDB.objects.order_by('-rate')
    return render(request, 'runoApp/runoListaweb.html', {'shelf': shelf})


def runoUusi(request):
    runouusi = RunoForm()
    if request.method == 'POST':
        runouusi = RunoForm(request.POST)
        if runouusi.is_valid():
            runouusi.save()
            return redirect('runoLista')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'runoLista'}}">reload</a>""")
    else:
        context = {
            'runouusi': runouusi
        }
        return render(request, 'runoApp/runoUusiweb.html', context)


def runoKorjaa(request, runo_id):
    runo_id = int(runo_id)
    try:
        runo_sel = RunoDB.objects.get(id=runo_id)
    except RunoDB.DoesNotExist:
        return redirect('runoLista')
    runo_form = RunoForm(request.POST or None, instance = runo_sel)
    if runo_form.is_valid():
       runo_form.save()
       return redirect('runoLista')
    return render(request, 'runoApp/runoUusiweb.html', {'runoUusi':runo_form})


def runoPoista(request, runo_id):
    runo_id = int(runo_id)
    try:
        runo_sel = RunoDB.objects.get(id=runo_id)
    except RunoDB.DoesNotExist:
        return redirect('runoLista')
    runo_sel.delete()
    return redirect('runoLista')


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
