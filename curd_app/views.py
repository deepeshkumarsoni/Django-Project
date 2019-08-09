from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Product_Data
from .forms import ProductCreateForm,ProductUpdateForm,ProductDeleteForm

def Home_View(request):
    return render(request,'home.html')

def Product_Create_View(request):
    if request.method == 'POST':
        cform = ProductCreateForm(request.POST)
        if cform.is_valid():
            pid  = request.POST.get('P_id')
            pname = request.POST.get('P_name')
            pcost = request.POST.get('P_cost')
            pcolor = request.POST.get('P_color')
            pclass = request.POST.get('P_class')

            data = Product_Data(
                P_id = pid,
                P_name = pname,
                P_cost = pcost,
                P_color =pcolor,
                P_class = pclass
            )
            data.save()
            cform = ProductCreateForm()
            return render(request, 'create.html', {'cform' : cform})
        else:
            return HttpResponse('Invalid Data')
    else:
        cform = ProductCreateForm()
        return render(request,'create.html',{'cform':cform})

def Product_Retrieve_View(request):

    products = Product_Data.objects.all()
    return render(request,'retrieve.html',{'products':products})

def Product_Update_View(request):
    if request.method == 'POST':
        uform = ProductUpdateForm(request.POST)
        if uform.is_valid():
         pid= request.POST.get('P_id')
         pcost = request.POST.get('P_cost')
         pid = Product_Data.objects.filter(P_id = pid)
         if not pid:
                return HttpResponse('Product Is Not Available')
         else:
            pid.update(P_cost = pcost)
            uform = ProductUpdateForm()
            return render(request, 'update.html', {'uform' : uform})
        else:
            return HttpResponse("Invalid Data")

    else:
        uform = ProductUpdateForm()
        return render(request,'update.html',{'uform':uform})

def Product_Delete_View(request):
    if request.method == 'POST':
        dform = ProductDeleteForm(request.POST)
        if dform.is_valid():
         pid= request.POST.get('P_id')
         pid = Product_Data.objects.filter(P_id = pid)
         if not pid:
                return HttpResponse('Product Is Not Available')
         else:
            pid.delete()
            dform = ProductDeleteForm()
            return render(request, 'delete.html',{'dform' : dform})
        else:
            return HttpResponse("Invalid Data")

    else:
        dform = ProductDeleteForm()
        return render(request,'delete.html',{'dform':dform})




