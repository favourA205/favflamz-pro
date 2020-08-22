from django.shortcuts import render,redirect
from .forms import RegistrationForm,signInform
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    context = {
        'formu': signInform
    }

    return render(request, 'base.html',context)

def reg_page(request):
    context = {
        'form':RegistrationForm
    }

    return render(request, 'regpage.html',context)

def addUser(request):
    register = RegistrationForm(request.POST)

    if register.is_valid():
        register.save()

    return redirect('base_home')

def page1(request):

    select1 = request.POST.get('search1')
    print(select1)
    select2 = request.POST.get('search2')
    print(select2)
    select3 = request.POST.get('search3')
    print(select3)
    select4 = request.POST.get('search4')
    print(select4)

    context = {
        'search1': select1,
        'search2': select2,
        'search3': select3,
        'search4': select4

    }

    return render(request, 'sub and yrs.html', context)




def instruction_page(request):
    return render(request,'instruction page.html')


def chemistry_page(request):
    baseurl ='https://myschool.ng/classroom/{}?exam_type=jamb&exam_year=2019'

    response = requests.get(baseurl)
    final_url = baseurl.format(quote_plus(select1))
    data = final_url
    print(data)

    print(final_url)
    jontext = {
         'g':data

     }


    return render(request, 'chemistry page.html',jontext)

