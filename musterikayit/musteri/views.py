from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Musteri
from .forms import MusteriForm
from django.core.paginator import Paginator, EmptyPage,  PageNotAnInteger

def musteri_index(request):
    musteri_list = Musteri.objects.all()
    paginator = Paginator(musteri_list, 25)
    page = request.GET.get('page')

    try:
        musteris = paginator.page(page)
    except PageNotAnInteger:
        musteris = paginator.page(1)
    except EmptyPage:
        musteris = paginator.page(paginator.num_pages)

    return render(request,'musteri/index.html',{'musteris':musteris})

def musteri_detail(request, id):
    musteri = get_object_or_404(Musteri, id=id)
    context = {
            'musteri':musteri,
    }

    return render(request, 'musteri/detail.html', context)

def musteri_create(request):
    form= MusteriForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
            'form':form,
    }
    return render(request, 'musteri/form.html', context)


def musteri_update(request, id):
    musteri = get_object_or_404(Musteri, id=id)
    form= MusteriForm(request.POST or None, instance=musteri)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(musteri.get_absolute_url())
    context=  {
            'form':form,
    }
    return render(request, 'musteri/form.html', context)


def musteri_delete(request,id):
    musteri= get_object_or_404(Musteri, id=id)
    musteri.delete()

    return redirect('index')

# Create your views here.

