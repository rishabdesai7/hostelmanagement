from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as l
from django.contrib.auth import logout as o
from django.db import connection
from hostalmanagement.models import applications,complaint
# Create your views here.
def index(request):
    return render(request,'hostalmanagement/index.html')
def login(request,msg= ''):
    return render(request,'hostalmanagement/login.html',{'message':msg})
def auth(request):
    id,pwd = request.POST['id'],request.POST['password']
    u = authenticate(username = id,password = pwd)
    if u:
        l(request,u)
        return dashboard(request)
    return login(request,'Invalid Credentails')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.username
        with connection.cursor() as cursor:
            cursor.execute('select * from users where id = '+id)
            k = cursor.fetchone()
            content = {
                'name' : k[2],
                'id' : k[0],
                'phone':k[6],
                'hostelno':k[4],
                'roomno':k[5]
            }
            return render(request,'hostalmanagement/sdash.html',content)
    return login(request,'Invalid Credentails')

def logout(request):
    o(request)
    return index(request)

def apply(request):
    id = request.user.username
    with connection.cursor() as cursor:
        cursor.execute('select hostel_no from users where id = ' + id)
        k = cursor.fetchone()
        if k[0] == -1:
            cursor.execute('select hostel_no,room_id from rooms where status = "free"')
            k = cursor.fetchall()
            return render(request,'hostalmanagement/apply.html',{'roomdata':k,'notalloted':'true'})
    return render(request, 'hostalmanagement/apply.html')
def application(request):
    hostel_no,room_no,st_id = request.POST['hostelno'],request.POST['roomno'],request.user.username
    k = applications(student_id = st_id,hostel_id  = hostel_no,room_id  = room_no,status = 'na')
    k.save()
    return dashboard(request)
def complaints(request):
    return render(request,'hostalmanagement/complaints.html')
def complain(request):
    id,text = request.user.username,request.POST['complaint']
    complaint(s_id = id,text = text).save()
    return dashboard(request)
def contact(request):
    return render(request, 'hostalmanagement/contact.html')

