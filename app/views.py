from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
def nameF(request):
    FO=NameForm()
    d={'FO':FO}
    if request.method=='POST':
        FD=NameForm(request.POST)
        if FD.is_valid():
            n=FD.cleaned_data['name']
            a=FD.cleaned_data['age']
            g=FD.cleaned_data['gender']
            c=FD.cleaned_data['course']
            data={'n':n,'a':a,'g':g,'c':c}
            return render(request,'form_data.html',data)
    return render(request,'nameF.html',d)


def topic_form(request):
    FO=TopicForm()
    d={'FO':FO}
    if request.method=='POST':
        FD=TopicForm(request.POST)
        if FD.is_valid():
            topic=FD.cleaned_data['tn']
            t=Topic.objects.get_or_create(topic_name=topic)[0]
            t.save()
            return HttpResponse('Data inserted')





    return render(request,'topic_form.html',d)