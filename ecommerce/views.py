from django.shortcuts import render,redirect
from core.models import Category,Product,Contact_us
from django.contrib.auth import authenticate, login
from core.models import UserCreationForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# creation header or footer
def Master(request):
    return render(request,'master.html') 

# home page 
def Index(request):
    category = Category.objects.all()#listing all categories
    product = Product.objects.all()#listing all product in categories
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    else:
        product = Product.objects.all()    
    context={  
        'category':category,
        'product':product
    }
    return render(request,'index.html',context)     

# login and signup
def signup(request):
  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form':form,
    }
    return render(request,'registration/signup.html',context)   

# add to cart
@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')  


# contact us page
def Contact_Page(request):
    if request.method == "POST":
        contact = Contact_us(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        contact.save()
    return render(request,'contact.html')

# all product detaile
def ProductDetails(request):
    category = Category.objects.all()
    product = Product.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    else:
        product = Product.objects.all()    
    context={  
        'category':category,
        'product':product
    }
    return render(request,'product.html',context)
# single product page
def ProductDetails_page(request,id):
    product = Product.objects.filter(id=id).first()
    context = {
        'product':product
    }
    return render(request,'product_detail.html',context)

# Search
def Search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains = query)
    context = {
        'product':product,
    }
    return render(request,'search.html',context)

