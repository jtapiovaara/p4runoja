from django.shortcuts import render
from .models import RunoDB
from django.shortcuts import render, redirect
from .forms import RunoForm
from django.http import HttpResponse

# Create your views here.

def runoLista(request):
    shelf = RunoDB.objects.order_by('-rate')
    return render(request, 'runoListaweb.html', {'shelf': shelf})

def runoUusi(request):
    runoUusi = RunoForm()
    if request.method == 'POST':
        runoUusi = RunoForm(request.POST)
        if runoUusi.is_valid():
            runoUusi.save()
            return redirect('runoLista')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'runoLista'}}">reload</a>""")
    else:
        return render(request, 'runoUusiweb.html', {'runoUusi': runoUusi})

# def runoKorjaa(request, runo_id):
#     runo_id = int(runo_id)
#     try:
#         runo_sel = RunoDB.objects.get(id = runo_id)
#     except RunoDB.DoesNotExist:
#         return redirect('runoLista')
#     runo_form = RunoForm(request.POST or None, instance = runo_sel)
#     if runo_form.is_valid():
#        runo_form.save()
#        return redirect('runoLista')
#     return render(request, 'runoUusiweb.html', {'runoUusi':runo_form})
#
# def runoPoista(request, runo_id):
#     runo_id = int(runo_id)
#     try:
#         runo_sel = RunoDB.objects.get(id = runo_id)
#     except RunoDB.DoesNotExist:
#         return redirect('runoLista')
#     runo_sel.delete()
#     return redirect('runoLista')