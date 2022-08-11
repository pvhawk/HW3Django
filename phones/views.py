from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    srt = request.GET.get('sort')
    phones = Phone.objects.all()
    print(srt)
    if srt == 'name':
        phones = sorted(phones, key=lambda phone: phone.name)
    if srt == 'min_price':
        phones = sorted(phones, key=lambda phone: phone.price)
    if srt == 'max_price':
        phones = sorted(phones, key=lambda phone: phone.price, reverse=True)

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):

    phones = Phone.objects.filter(slug=slug)

    template = 'product.html'
    context = { 'phone': phones[0]
        }

    return render(request, template, context)
