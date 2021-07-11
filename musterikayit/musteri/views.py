from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.core.paginator import Paginator, EmptyPage,  PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from .models import Musteri
from .forms import MusteriForm


def customer_index(request):
    customer_list = Musteri.objects.all()
    query = request.GET.get('q')
    if query:
        customer_list = customer_list.filter(
                Q(isim__icontains = query) |
                Q(soyisim__icontains = query) |
                Q(tc__icontains = query) |
                Q(id__icontains = query) |
                Q(sehir__icontains = query) |
                Q(ilce__icontains = query))

    paginator = Paginator(customer_list, 25)
    page = request.GET.get('page')

    try:
        musteris = paginator.page(page)
    except PageNotAnInteger:
        musteris = paginator.page(1)
    except EmptyPage:
        musteris = paginator.page(paginator.num_pages)

    return render(request,'musteri/index.html',{'musteris':musteris})

def customer_detail(request, id):
    musteri = get_object_or_404(Musteri, id=id)
    context = {
            'musteri':musteri,
    }

    return render(request, 'musteri/detail.html', context)

def customer_create(request):
    form= MusteriForm(request.POST or None)
    if form.is_valid():
        musteri=form.save()
        messages.success(request, 'Başarılı bir şekilde ekleme yapıldı')
        return HttpResponseRedirect(musteri.get_absolute_url())

    context = {
            'form':form,
    }
    return render(request, 'musteri/form.html', context)

def customer_update(request, id):
    musteri = get_object_or_404(Musteri, id=id)
    form= MusteriForm(request.POST or None, instance=musteri)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde ekleme yapıldı')
        return HttpResponseRedirect(musteri.get_absolute_url())
    context=  {
            'form':form,
    }
    return render(request, 'musteri/form.html', context)

def customer_delete(request,id):
    musteri= get_object_or_404(Musteri, id=id)
    musteri.delete()

    return redirect('index')


