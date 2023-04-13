
from django.http import HttpResponse
from .models import books
from .models import students
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.apps import apps
# Create your views here.
def main(request):
    bks = books.objects.all()
    return render(request, 'list.html',{'bks':bks})

def rent(request):
    return render(request, 'rent.html')


def result(request):
    res = "Success"
    check = books.objects.filter(name = request.POST["bookname"]).exists()
    stu = students.objects.filter(netid = request.POST["netid"])
    if len(stu) == 2:
        res = "Each student borrows at most 2 books each time"
    elif check != True:
        res = "Error: no such book exist"
    else:
        bk = books.objects.get(name = request.POST["bookname"])
        if bk.quantity == 0:
            res = "Error: out of stock"
        else:
            bk.quantity -= 1
            bk.save()
            students.objects.create(netid = request.POST["netid"],bookname = request.POST["bookname"])

    return render(request,"result.html",{"res":res})


def home(request):
    return render(request, 'home.html')


def returnbooks(request):
    if request.method == 'POST':
        netid = request.POST['netid']
        bookname = request.POST['bookname']
        bk = books.objects.get(name = bookname)
        check = students.objects.filter(netid = netid, bookname = bookname).exists()
        if check:
            students.objects.filter(netid = netid, bookname = bookname).delete()
            bk.quantity += 1
            bk.save()
            return redirect("/books/home/")
        else:
            messages.info(request,"no such record")
            return redirect("/books/returnbooks/")
    else:
        return render(request,"returnbooks.html")