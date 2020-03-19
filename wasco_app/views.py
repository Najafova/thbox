from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from wasco_app.models import DeviceSettings, DeviceData, DeviceLimit, LogData
from django.utils import timezone
from .forms import DeviceLimitForm


# Create your views here.

# def notification():
#     info = []
#     notif_dict = {}
#     data = DeviceData.objects.all()
#     for notif in data:
#         if notif.bin_state > 75:
#             info.append({
#                 "data":"Wasco:{} ({}vt - {}%)".format(notif.imei_code, notif.battery, notif.bin_state)
#             })
#     notif_dict["notif_list"] = info
#     return notif_dict


# def color():
#     pass
        

def index(request):
    context = {}
    # context = notification()
    context["marker"] = DeviceData.objects.all()
    data = DeviceSettings.objects.all()
    # d_data = DeviceSettings.objects.all()
    result = []
    test = []
    order = 0
    for item in data:
        order = order + 1
        try:
            d_data = DeviceData.objects.get(imei_code=item.imei_code)

            if d_data.bin_state<25:
                color = "bg-success"
            elif d_data.bin_state<51:
                color = "yellow"
            elif d_data.bin_state<75:
                color = "orange"
            else:
                color = "bg-danger"
                
        
            result.append({
                "coords": {"lat": item.latitude, "lng": item.longitude},
                "text": "{} {} {} {} {}".format(order, item.imei_code or int(0), d_data.battery or int(0), d_data.bin_state or int(0), d_data.request_time or int(0)).split(),
                # "battery": "bg-danger" if (int(d_data.bin_state) or 0) >= 75  else "bg-success",
                "battery": color,
                "device_icon": d_data.device_icon()
            })
        except DeviceData.DoesNotExist:
            result.append({
            "coords": {"lat": item.latitude, "lng":item.longitude},
            "text": "{} {} {} {} {}".format(order, item.imei_code, int(0), int(0), d_data.request_time).split(),
            "battery": "bg-danger",
            "device_icon": "/static/wasco/images/th.png"
            })
    context["object_list"] = result

    context["form"] = DeviceLimitForm
    if request.method == "POST":
        form = DeviceLimitForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("index")
        else:
            context["form"] = form
    return render(request, "index.html", context)



@csrf_exempt
def data(request):
    limit = ""
    limit = DeviceLimit.objects.last()
    uplimit = limit.up_limit
    downlimit = limit.down_limit

    taym = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
    test = request.body.decode()
    print(test)
    incoming_data = request.body.decode().strip()
    
    # request.GET.get("query").strip() 
    # request.body.decode().strip()
    if ',' in incoming_data:
        parsed_data = incoming_data.split(',')
    else:
        parsed_data = incoming_data

    print(parsed_data[2])


    LogData.objects.filter(imei_code=parsed_data[2]).create(imei_code=parsed_data[2],battery=parsed_data[0],bin_state=int(parsed_data[1]),request_time=taym)


    if DeviceSettings.objects.filter(imei_code=parsed_data[2]) and DeviceData.objects.filter(imei_code=parsed_data[2]):
        DeviceData.objects.filter(imei_code=parsed_data[2]).update(battery=parsed_data[0],bin_state=int(parsed_data[1]),request_time=taym)
        print("Update olundu")

    elif DeviceSettings.objects.filter(imei_code=parsed_data[2]) and not DeviceData.objects.filter(imei_code=parsed_data[2]):
        DeviceData.objects.filter(imei_code=parsed_data[2]).create(imei_code=parsed_data[2],battery=parsed_data[0],bin_state=int(parsed_data[1]),request_time=taym)
        print("Elave olundu")
    else:
        print("Xeta baş verdi. Cihaz tanınmadı")
    return HttpResponse("%s,%s," %(uplimit,downlimit))