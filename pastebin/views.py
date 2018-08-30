from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
from django import template
from django.utils import timezone

from django.shortcuts import render,get_object_or_404
from pastebin.forms import input,Authentic,input_logged_in
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from pastebin.models import paste,paste_logged_in
from datetime import datetime,date,timedelta
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def front_page(request):
 return render(request,"pastebin/front_page.html") 



def main_page(request):
    form=input()
    mypaste=paste.objects.all()
    mypaste = sorted(mypaste,key=lambda x:x.url,reverse=True)

    if request.method=="POST":
        form=input(request.POST)
        mydate=request.POST.get("date",)
        ins = form.save(commit=False)
        ins.expiration_date=mydate
        year,month,day=map(int,mydate.split("-"))
        mydate=date(year,month,day)
        diff=mydate-date.today()
        if diff.days<0:
            return render(request,"pastebin/return_invalid_date.html")
        else:
        #date_i=date.today()-mydate
         if form.is_valid():
            latest_model=form.save()
            var3=latest_model.url
            return render(request,"pastebin/ss.html",{"form":form,"var3":var3, }) 
         else:
               return render(request,"pastebin/return_valid_data.html")   
    return render(request,"pastebin/paste.html",{"form":form ,"mypaste":mypaste[:10]}) 
@login_required
def main_loggedin_page(request):
   form=input_logged_in()

   usernam=request.user.username
   var=form.save(commit=False)
   var.owner=usernam
   print(usernam)
   mypaste=paste_logged_in.objects.filter(owner=usernam)
   mypaste = sorted(mypaste,key=lambda x:x.url,reverse=True)
   #mypaste=paste_logged_in.objects.all() 
   if request.method=="POST":
        form=input_logged_in(request.POST)
        mydate=request.POST.get("date",)

        var=form.save(commit=False)
        var.expiration_date=mydate
        year,month,day=map(int,mydate.split("-"))
        mydate=date(year,month,day)
        diff=mydate-date.today()
        var.owner=usernam
        if diff.days<0:
            return render(request,"pastebin/return_invalid_date_log.html")
        else:
         if form.is_valid():
            latest_model=form.save()
            var3=latest_model.url
            return render(request,"pastebin/ss_logged_in.html",{"form":form,"var3":var3,"username":usernam}) 
         else:
               return render(request,"pastebin/return_valid_datalog.html")

   return render(request,"pastebin/paste_loggedin.html",{"form":form,"username":usernam ,"mypaste":mypaste[:50],}) 



def content_fetch(request,url_no):
     content_object=paste.objects.get(pk = url_no)
     mydate = content_object.expiration_date
     
     diff=mydate-date.today()
     print(diff.days)
     if diff.days<0:
            return render(request,"pastebin/return_link_expired.html")
     else:
         return render(request,"pastebin/fetching_content.html",{"content_object":content_object,"var3":url_no ,"days":diff.days})

def content_fetch_logged_in(request,url_no):
    content_object=paste_logged_in.objects.get(pk = url_no)
    mydate = content_object.expiration_date
    diff=mydate-date.today()
    usernam=request.user.username
    if diff.days<0:
            return render(request,"pastebin/return_link_expired.html")
    else:
        return render(request,"pastebin/fetching_content_logged_in.html",{"content_object":content_object ,"var3":url_no,"username":usernam ,"days":diff.days}) 


def user_signup(request):
    registered = False
    
    if request.method=="POST":
     auth=Authentic(request.POST )

     if auth.is_valid():
         auth=auth.save(commit=False)
         auth.set_password(auth.password)   
         #hashing the password
         auth.save()
         registered=True


     else :
         print("error")
    else:
        auth=Authentic()     
    return render(request,"pastebin/signup.html",{"auth":auth,"registered":registered })        


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)


        if user:
            login(request,user)
            return HttpResponseRedirect(reverse("pastebin:main_loggedin_page",))
        else:
            return render(request,"pastebin/return_invalid_user.html")
    else :
        return render(request,"pastebin/login.html",{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("pastebin:main_page",))


def paste_edit(request,pk):
    my_record = paste.objects.get(url=pk)
    if my_record.editable==False :
        return render(request,"pastebin/return_edit_excess.html")
    else:
     form = input(instance=my_record)
    
     if request.method=="POST":
        form = input(request.POST, instance=my_record)
        form.save()
        return render(request,"pastebin/return_edit.html")
     return render(request,"pastebin/paste_edit.html",{"form":form,"pk":pk})

def paste_edit_logged_in(request,pk):
    my_record = paste_logged_in.objects.get(url=pk)
    if my_record.editable==False:
        return render(request,"pastebin/return_edit_excesslog.html")
    else:

     form = input_logged_in(instance=my_record)
     if request.method=="POST":
        form = input_logged_in(request.POST, instance=my_record)
        form.save()
        return render(request,"pastebin/return_edit_log.html")
     return render(request,"pastebin/paste_edit_logged_in.html",{"form":form,"pk":pk}) 

