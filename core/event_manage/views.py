from django.shortcuts import render ,redirect

from .models import Events , CrudUser
from django.views.generic import TemplateView, View, DeleteView
from django.http import HttpResponseRedirect
from django.http import JsonResponse
#Create your views here.

def event(request):
    all_events = Events.objects.all()
    get_event_types = Events.objects.only('event_type')

    # if filters applied then get parameter and filter based on condition else return object
    # if request.GET:  
    #     event_arr = []
    #     if request.GET.get('event_type') == "all":#
    #         all_events = Events.objects.all()
    #     else:   
    #         all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))
            
    #     for i in all_events:
    #         event_sub_arr = {}
    #         event_sub_arr['title'] = i.event_name
    #         start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
    #         end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
    #         event_sub_arr['start'] = start_date
    #         event_sub_arr['end'] = end_date
    #         event_arr.append(event_sub_arr)
    #     return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,
        #"get_event_types":get_event_types,

    }
    return render(request,'core/templates/calendar.html',context)



def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'core/templates/calendar2.html',context)

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)





class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)    




def add_event_to_end(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    Events = Events(name=str(event_name), start=start_date, end=end_date)
    Events.save()
    data = {}
    return JsonResponse(data)        


# class newevent(View):
#     def  get(self, request):
def newevent(request):
    if request.method=='POST':
        event_name = request.POST['event_name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        obj = Events.objects.create(
            event_name = event_name,
            start_date = start_date,
            end_date = end_date,
        
        )

        event = {'id':obj.event_id,'event_name':obj.event_name,'start_date':obj.start_date,'end_date':obj.end_date}

        data = {
            'event': event
        }
        print(request.POST) 
        #return JsonResponse(data)
        #return HttpResponseRedirect('/newevent')
        return redirect ('/event')
    return redirect ('/event')




def sessionDetail(request,id):
    events = models.Events.objects.get(event_id=id)
    if request.method == 'POST':
        form = forms.SessionDetail(request.POST, instance=events)
        if form.is_valid():
           form.save()
           return redirect("manage-event")
           
    else:
        form = forms.SessionDetail(instance=events)
    return render(request, 'core/templates/sessionDetail.html',{'form':form})       