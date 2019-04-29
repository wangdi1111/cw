from django.shortcuts import render,redirect,HttpResponse
from cm.forms import AddBook
from web import models
from django.urls import reverse

# Create your views here.
def showbooks(request):
    all_books_obj = models.Books.objects.all()
    return render(request,'showbooks.html',{'all_books_obj':all_books_obj})
def deletebook(request,pk):
    models.Books.objects.get(pk=pk).delete()
    return redirect(reverse('showbooks'))
def changebook(request,pk=None):
    obj = models.Books.objects.filter(pk=pk).first()
    ret = AddBook(instance=obj)
    if request.method == "POST":
        ret = AddBook(data=request.POST,instance=obj)
        if ret.is_valid():
            ret.save()
            return redirect(reverse('showbooks'))
    return render(request,'addbook.html',{'form':ret})




