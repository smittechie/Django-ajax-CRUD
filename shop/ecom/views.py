from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Mobile


# Create your views here.

def mobiles(request):
    mobile_data = Mobile.objects.all()
    return render( request, 'index.html' , {'data_mob':mobile_data })

@csrf_exempt
def save_mobile(request):
    try:
        mobile_name = request.POST['mobile']
        ram = request.POST['ram']
        colour = request.POST['colour']
        price = request.POST['price']
        Mobile.objects.create(Mobile=mobile_name,RAM=ram , Colour=colour,Price=price)

        return JsonResponse({"code" :1 , "data" : "Sucess"})
    except Exception as e:
        return JsonResponse({"code":0,"msg":"Error occured"})
