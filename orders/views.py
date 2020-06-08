from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import OrderForm
from .models import Order
from evaluate.models import SubCategory
from evaluate.models import EvaluationCompany,EvaluationOrder
import random

@login_required(login_url="/user/login")
def addOrder(request):
    form = OrderForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.save()

        messages.success(request, "Sifarişiniz uğurla həyata keçirildi!")
        return redirect("/orders_panel/ordersview")
    context = {
        "form" : form
    }
    return render(request, "addorder.html", context)

@login_required(login_url="/user/login")
def ordersView(request):
    orders_icra = Order.objects.filter(company_name_id=1)
    orders_mahkama = Order.objects.filter(company_name_id=2)
    context = {
        "orders_icra" : orders_icra,
        "orders_mahkama" : orders_mahkama,
    }
    return render(request, "ordersview.html", context)

@login_required(login_url="/user/login")
def viewOrder(request,id):
    order = get_object_or_404(Order, id = id)
    if request.method == "POST":
        if order.is_send == False:
            evaluation_companies = EvaluationCompany.objects.all()
            subcategory_name = SubCategory.objects.get(id = order.subcategory_name_id)
            choosen_companies = random.sample(list(evaluation_companies),k=3)
            choosen_company_1 = choosen_companies[0]
            choosen_company_2 = choosen_companies[1]
            choosen_company_3 = choosen_companies[2]
            
            newEvaOrder = EvaluationOrder(order_name = order.order_name,subcategory_name = subcategory_name,order_law_decision=order.order_law_decision,order_deptor=order.order_deptor,order_claimant=order.order_claimant,order_information=order.order_information,order_document=order.order_document,order_keep_date_location=order.order_keep_date_location,order_mobile=order.order_mobile)
            newEvaOrder.save()

            newEvaOrder.company_name.add(choosen_company_1,choosen_company_2,choosen_company_3)

            order.is_send = True
            order.save()

            messages.success(request,"Sifarişiniz uğurla göndərildi!")
            return redirect("/orders_panel/ordersview")
        else:
            messages.info(request,"Sifarişinizi artıq göndərmisiniz!")
            return redirect("/orders_panel/ordersview")
    else:
        messages.info(request,"Sifarişinizi göndərərkən xəta baş verdi!")
        return redirect("/orders_panel/ordersview")

@login_required(login_url="/user/login")
def chooseOrder(request, id):
    order = get_object_or_404(Order, id = id)
    if request.method == "POST":
        price = request.POST.get("price")
        print(price)
        if price == str(order.price_one) or price == str(order.price_two) or price == str(order.price_three):
            order.choosen_price = price
            order.is_choosed = True
            order.save()
            messages.success(request,"Əmlak üzər qiymətinizi seçdiniz və təstiqlədiniz!")
            return redirect("/orders_panel/ordersview")
        else:
            messages.info(request,"Seçdiyiniz qiymət sizə təqdim edilən qiymətlərə uyğun deyil!")
            return redirect("/orders_panel/ordersview")
    else:
        messages.info(request,"Qiymət seçimində xəta baş verdi!")
        return redirect("/orders_panel/ordersview")