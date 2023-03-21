from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def Index(request):
    return render(request, 'index.html')


def AddInfo(request):
    if request.method == "POST":
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        logo = request.FILES['logo']
        Info.objects.create(
            logo=logo,
            text_ru=text_ru,
            text_uz=text_uz
        )
        return redirect('add-info')
    return render(request, 'add-info.html')


def ListInfo(request):
    context = {
        'info': Info.objects.all().order_by('-id')
    }
    return render(request, 'list-info.html', context)


def EditInfo(request,pk):
    if request.method == 'POST':
        i = Info.objects.get(id=pk)
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        logo = request.FILES['logo']
        i.text_uz = text_uz
        i.text_ru = text_ru
        i.logo = logo
        i.save()
        return redirect('list-info')
    return render(request, 'edit-info.html')


def DeleteInfo(request,pk):
    Info.objects.get(id=pk).delete()
    return redirect('list-info')


def AddSocialMedia(request):
    if request.method == "POST":
        link = request.POST.get('link')
        img = request.FILES['img']
        SocialMedia.objects.create(
            img = img,
            link = link
        )
        return redirect('add-social-media')
    return render(request, 'add-social-media.html')


def ListSocialMedia(request):
    context = {
        'social': SocialMedia.objects.all().order_by('-id')
    }
    return render(request, 'list-social-media.html', context)


def EditSocialMedia(request,pk):
    if request.method == 'POST':
        i = SocialMedia.objects.get(id=pk)
        link = request.POST.get('link')
        img = request.FILES['img']
        i.link = link
        i.img = img
        i.save()
        return redirect('list-social-media')
    return render(request, 'edit-social-media.html')


def DeleteSocialMedia(request,pk):
    SocialMedia.objects.get(id=pk).delete()
    return redirect('list-social-media')


def ListOrder(request):
    context = {
        'order': Order.objects.all().order_by('-id')
    }
    return render(request, 'list-order.html', context)


def EditOrder(request,pk):
    if request.method == 'POST':
        i = Order.objects.get(id=pk)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        i.name = name
        i.phone= phone
        i.save()
        return redirect('list-order')
    return render(request, 'edit-order.html')


def DeleteOrder(request,pk):
    Order.objects.get(id=pk).delete()
    return redirect('list-order')


def AddProduct(request):
    if request.method == "POST":
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        price = request.POST.get('price')
        img = request.FILES['img']
        Product.objects.create(
            img = img ,
            text_uz = text_uz ,
            text_ru = text_ru ,
            price = price
        )
        return redirect('add-product')
    return render(request, 'add-product.html')


def ListProduct(request):
    context = {
        'product': Product.objects.all().order_by('-id')
    }
    return render(request, 'list-product.html', context)


def EditProduct(request,pk):
    if request.method == 'POST':
        t = Product.objects.get(id=pk)
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        price = request.POST.get('price')
        img = request.FILES['img']
        t.text_uz = text_uz
        t.text_ru = text_ru
        t.price = price
        t.img = img
        t.save()
        return redirect('list-product')
    return render(request, 'edit-product.html')


def DeleteProduct(request,pk):
    Product.objects.get(id=pk).delete()
    return redirect('list-product')


def AddAboutProduct(request):
    if request.method == "POST":
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        img = request.FILES['img']
        AboutProduct.objects.create(
            img=img,
            text_ru=text_ru,
            text_uz=text_uz
        )
        return redirect('add-about-product')
    return render(request, 'add-about-product.html')


def ListAboutProduct(request):
    context = {
        'about': AboutProduct.objects.all().order_by('-id')
    }
    return render(request, 'list-about-product.html', context)


def EditAboutProduct(request,pk):
    if request.method == 'POST':
        i = AboutProduct.objects.get(id=pk)
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        img = request.FILES['img']
        i.text_uz = text_uz
        i.text_ru = text_ru
        i.img = img
        i.save()
        return redirect('list-about-product')
    return render(request, 'edit-about-product.html')


def DeleteAboutProduct(request,pk):
    AboutProduct.objects.get(id=pk).delete()
    return redirect('list-about-product')


def AddAboutCompany(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        photo = request.FILES['photo']
        AboutCompany.objects.create(
            photo = photo,
            text_ru = text_ru,
            text_uz = text_uz,
            title_ru = title_ru,
            title_uz = title_uz
        )
        return redirect('add-about-company')
    return render(request, 'add-about-company.html')


def ListAboutCompany(request):
    context = {
        'company': AboutCompany.objects.all().order_by('-id')
    }
    return render(request, 'list-about-company.html', context)


def EditAboutCompany(request,pk):
    if request.method == 'POST':
        i = AboutCompany.objects.get(id=pk)
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        photo = request.FILES['photo']
        i.text_uz = text_uz
        i.text_ru = text_ru
        i.title_uz = title_uz
        i.title_ru = title_ru
        i.photo = photo
        i.save()
        return redirect('list-about-company')
    return render(request, 'edit-about-company.html')


def DeleteAboutCompany(request,pk):
    AboutCompany.objects.get(id=pk).delete()
    return redirect('list-about-company')


def AddWhoUse(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        WhoUse.objects.create(
            title_uz = title_uz,
            title_ru = title_ru
        )
        return redirect('add-who-use')
    return render(request, 'add-who-use.html')


def ListWhoUse(request):
    context = {
        'list': WhoUse.objects.all().order_by('-id')
    }
    return render(request, 'list-who-use.html', context)


def EditWhoUse(request,pk):
    if request.method == 'POST':
        i = WhoUse.objects.get(id=pk)
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        i.title_uz = title_uz
        i.title_ru = title_ru
        i.save()
        return redirect('list-who-use')
    return render(request, 'edit-who-use.html')


def DeleteWhoUse(request,pk):
    WhoUse.objects.get(id=pk).delete()
    return redirect('list-who-use')


def AddHowtoUse(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        img = request.FILES['img']
        HowToUse.objects.create(
            img = img,
            text_ru = text_ru,
            text_uz = text_uz,
            title_ru = title_ru,
            title_uz = title_uz
        )
        return redirect('add-how-to-use')
    return render(request, 'add-how-to-use.html')


def ListHowtoUse(request):
    context = {
        'how': HowToUse.objects.all().order_by('-id')
    }
    return render(request, 'list-how-to-use.html', context)


def EditHowtoUse(request,pk):
    if request.method == 'POST':
        i = HowToUse.objects.get(id=pk)
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        img = request.FILES['img']
        i.text_uz = text_uz
        i.text_ru = text_ru
        i.title_uz = title_uz
        i.title_ru = title_ru
        i.img = img
        i.save()
        return redirect('list-how-to-use')
    return render(request, 'edit-how-to-use.html')


def DeleteHowtoUse(request,pk):
    HowToUse.objects.get(id=pk).delete()
    return redirect('list-how-to-use')


def AddFact(request):
    if request.method == "POST":
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        number = request.POST.get('number')
        Fact.objects.create(
            text_uz = text_uz ,
            text_ru = text_ru ,
            number = number
        )
        return redirect('add-fact')
    return render(request, 'add-fact.html')


def ListFact(request):
    context = {
        'fact': Fact.objects.all().order_by('-id')
    }
    return render(request, 'list-fact.html', context)


def EditFact(request,pk):
    if request.method == 'POST':
        t = Fact.objects.get(id=pk)
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        number = request.POST.get('number')
        t.text_uz = text_uz
        t.text_ru = text_ru
        t.number = number
        t.save()
        return redirect('list-fact')
    return render(request, 'edit-fact.html')


def DeleteFact(request,pk):
    Fact.objects.get(id=pk).delete()
    return redirect('list-fact')