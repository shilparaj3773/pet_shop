from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from petshop_app.forms import UserForm, customerForm, sellerForm, AddpetForm
from petshop_app.models import pet, customer, orderplaced, payment


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'registration/login.html')


def cxhome(request):
    return render(request, 'cx/index.html')


def sellerhome(request):
    return render(request, 'seller/index.html')


def userview(request):
    user = request.user
    if user.is_staff:
        return redirect('admhome')
    elif user.is_customer:
        return redirect('cxhome')
    elif user.is_seller:
        return redirect('sellerhome')
    else:
        return redirect('index')


def admhome(request):
    return render(request, 'adm/index.html')


def signup1(request):
    form = UserForm()
    n_form = customerForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = customerForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('signup1')
    return render(request, 'register1.html', {'form': form, 'n_form': n_form})


def signup2(request):
    form = UserForm()
    r_form = sellerForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        r_form = sellerForm(request.POST, )
        if form.is_valid() and r_form.is_valid():
            user = form.save(commit=False)
            user.is_seller = True
            user.save()
            s = r_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('signup2')
    return render(request, 'register2.html', {'form': form, 'r_form': r_form})


def add_pet(request):
    form = AddpetForm()

    if request.method == 'POST':
        form = AddpetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'pet Add Successfully')
            return redirect('add_pet')
    return render(request, 'seller/add_pet.html', {'form': form})


def view_pet(request):
    dataset = pet.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'seller/view_pet.html', context)


def update_p(request, id=None):
    data = pet.objects.get(id=id)
    form = AddpetForm(instance=data)
    if request.method == 'POST':
        form = AddpetForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, ' updated Successfully')
            return redirect('view_pet')

    return render(request, 'seller/update_pet.html', {'form': form})


def viewpet(request):
    dataset = pet.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'cx/viewpet.html', context)


def delete_pet(request, id=None):
    data = pet.objects.get(id=id)
    data.delete()
    return redirect('view_pet')


def add_order(request, id=None):
    u = customer.objects.get(user=request.user)
    accessory = pet.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        description = request.POST.get('description')
        picture = request.POST.get('picture')
        ob = orderplaced()
        ob.title = title
        ob.price = price
        ob.category = category
        ob.description = description
        ob.picture = picture
        ob.customer = u
        ob.save()
        messages.info(request, 'Requested')
        return redirect('view_order')

    return render(request, 'cx/add_order.html', {'key': accessory})


def view_order(request):
    dataset = orderplaced.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'cx/view_order.html', context)


def viewpet_order(request):
    dataset = orderplaced.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'seller/viewpet_order.html', context)


def confirm_order(request, id):
    req = orderplaced.objects.get(id=id)
    req.order_status = 1

    req.save()

    messages.info(request, 'Approved  Application')
    return redirect('viewpet_order')


def rej_order(request, id):
    req = orderplaced.objects.get(id=id)
    req.order_status = 2
    req.save()
    return redirect('viewpet_order')


def delete_order(request, id=None):
    data = orderplaced.objects.get(id=id)
    data.delete()
    return redirect('view_order')

#
# def view_payment(request, id=None):
#     u = customer.object.get(user=request.user)
#     accessory = orderplaced.objects.get(id=id)
#     if request.method == 'POST':
#         shipping_address = request.POST.get('shipping_address')
#         price = request.POST.get('price')
#         card_number = request.POST.get('card_number')
#         cvv = request.POST.get('cvv')
#         date = request.POST.get('date')
#         ob = payment()
#         ob.shipping_address = shipping_address
#         ob.price = price
#         ob.card_number = card_number
#         ob.cvv = cvv
#         ob.date = date
#         ob.custom = u
#         ob.payment_status = 1
#         ob.save()
#         messages.info(request, 'Requested')
#         return redirect('view_payment')
#
#     return render(request, 'cx/cx_paymant.html', {'key':accessory})

def payments(request, id):
    u = customer.objects.get(user=request.user)
    accessory = orderplaced.objects.get(id=id)
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address')
        price = request.POST.get('price')
        card_number = request.POST.get('card_number')
        cvv = request.POST.get('cvv')
        date = request.POST.get('date')

        ob = payment()

        ob.shipping_address = shipping_address
        ob.price = price
        ob.card_number = card_number
        ob.cvv = cvv
        ob.date = date
        ob.custom = u

        ob.save()
        messages.info(request, 'orderplaced successfully')
        return redirect('cxhome')

    return render(request, 'cx/payment.html', {'key': accessory})



