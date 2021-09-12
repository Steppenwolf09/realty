from django.shortcuts import render, redirect
from .models import *
from django.views.generic import TemplateView, ListView
from itertools import groupby
from .forms import HouseForm

# Create your views here.
def mainpage (request):
    return render(request, 'home/home.html')

def hata(request,id_h):
    id=id_h
    return render(request, 'home/hata.html', locals())



def detail(request):
    house =House.objects.all()
    return render(request, 'home/hata.html', {'data':house})

def create(request):
    error = ""
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail')
        else:
            error = "FORM неверная"

    form = HouseForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'home/create.html', data)


def allhouses (request):
    houses=House.objects.all()
    photos=Photo.objects.all()
    locations=Location.objects.all()
    zone=Zone.objects.all()
    status=Status.objects.all()
    aim=Aim.objects.all()
    source=Source_of_proposal.objects.all()


    return render(request, 'home/hata.html', locals())


class SearchResultsView(ListView):
    model = Photo
    template_name = 'home/hata.html'


    def get_queryset(self):

        query = self.request.GET.get('q')
        object_list = Photo.objects.filter(house__name__iregex=r'.*([а-яА-Я]+)*%s([а-яА-Я]+)*.*' %query, is_main=True)


        if (object_list):


            return object_list
        else:
            object_list = Photo.objects.filter(house__descrip__iregex=r'.*([а-яА-Я]+)*%s([а-яА-Я]+)*.*' %query, is_main=True)

            return object_list


class FilterResultsView(ListView):
    model = House
    template_name = 'home/hata.html'

    def get_queryset(self):
        price1 = self.request.GET.get('price1')
        price2 = self.request.GET.get('price2')
        square1 = self.request.GET.get('square1')
        square2 = self.request.GET.get('square2')
        Esquare1 = self.request.GET.get('Esquare1')
        Esquare2 = self.request.GET.get('Esquare2')
        locat = []

        locat = self.request.GET.getlist('locat[]')
        status = self.request.GET.getlist('status')
        aim = self.request.GET.get('aim')
        period = self.request.GET.get('period')
        source = self.request.GET.get('source')


        if aim == "Продажа":
            period = ""


        if (price1 == ''):
            price1 = 0
        if (price2 == ''):
            price2 = 999999999
        if (square1 == ''):
            square1 = 0
        if (square2 == ''):
            square2 = 999999999
        if (Esquare1 == ''):
            Esquare1 = 0
        if (Esquare2 == ''):
            Esquare2 = 999999999

        if not status:
            status=[1,2,3]



        object_list = []

        if locat:

            for z in locat:

                for s in status:

                    object = (House.objects.filter(price__range=(price1, price2), square__range=(square1, square2),
                                                   square_of_area__range=(Esquare1, Esquare2), zone__name=z,
                                                   status__id=s, aim__aim=aim, aim__period=period, source__source=source))

                    if object:
                        object_list.append(object)



        else:

            for s in status:

                object = (House.objects.filter(price__range=(price1, price2), square__range=(square1, square2),
                                               square_of_area__range=(Esquare1, Esquare2),
                                               status__id=s, aim__aim=aim, aim__period=period, source__source=source))
                if object:
                    object_list.append(object)



        return object_list




