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
        id = request.POST.get("id")
        mobile_name = request.POST['mobile']
        ram = request.POST['ram']
        colour = request.POST['colour']
        price = request.POST['price']

        if id is not None:
            mobile = Mobile.objects.get(id =int(id))
            mobile.Mobile= mobile_name
            mobile.Colour = colour
            mobile.RAM = ram
            mobile.Price = price
            mobile.save()
            return JsonResponse({"code": 1, "data": mobile.id})

        mobile = Mobile.objects.create(Mobile=mobile_name,RAM=ram , Colour=colour,Price=price)

        return JsonResponse({"code" :1 , "data" : mobile.id})
    except Exception as e:
        return JsonResponse({"code":0,"msg":"Error occured"})


@csrf_exempt
def delete_mobile(request):
    id = request.POST.get("id")
    mob = Mobile.objects.get(id=int(id))
    mob.delete()
    return JsonResponse({"detail": f"Successfully Deleted {mob.Mobile}"})