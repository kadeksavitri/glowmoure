import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import ProductDetailForm
from main.models import ProductDetail
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):

    context = {
        'name': request.user.username,
        'npm' : '2306203236',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductDetailForm(request.POST, request.FILES)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    else:
        form = ProductDetailForm()

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = ProductDetail.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# def show_json(request):
#     data = ProductDetail.objects.filter(user=request.user)
#     return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json(request):
    products = ProductDetail.objects.filter(user=request.user)
    product_list = []
    
    for product in products:
        product_data = {
            'id': product.pk,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'stock': product.stock,
            'image_url': product.image.url if product.image else None,  # Add image URL here
        }
        product_list.append(product_data)
    
    return JsonResponse(product_list, safe=False)


def show_xml_by_id(request, id):
    data = ProductDetail.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductDetail.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = ProductDetail.objects.get(pk=id)
    
    if request.method == "POST":
        form = ProductDetailForm(request.POST, request.FILES, instance=product)  # Menyertakan request.FILES
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = ProductDetailForm(instance=product)

    context = {'form': form}
    return render(request, 'edit_product.html', context)


def delete_product(request, id):
    product = ProductDetail.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def home(request):
    return HttpResponse("<h1>Welcome to Home</h1>")

def candle(request):
    return HttpResponse("<h1>Welcome to Candle Page</h1>")

def light(request):
    return HttpResponse("<h1>Welcome to Light Page</h1>")

def about_us(request):
    return HttpResponse("<h1>About Us</h1>")

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = request.POST.get("description")
    stock = request.POST.get("stock")
    category = request.POST.get("category")
    image = request.FILES.get("image")
    user = request.user

    new_product = ProductDetail(
        name=name, price=price,
        description=description,
        stock=stock, category=category,
        image=image,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)