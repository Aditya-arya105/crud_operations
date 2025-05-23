from django.shortcuts import render,redirect
from .models import Employee
# from django.shortcuts import render

# def home(Request):
#     if(Request.method=="POST"):
#         search=Request.POST.get("search")
#         data=Employee.objects.filter(name__icontains=search)
#     else:
#         data=Employee.objects.all()
#         return redirect('/')
#     return render(Request,"index.html",{'data':data})


def home(Request):
    if Request.method == "POST":
        search = Request.POST.get("search")
        if search:
            Request.session['search'] = search  # session में save करो
        return redirect('/')  # GET method से reload करो

    # GET request पर:
    search = Request.session.pop('search', None)  # session से निकालो और हटा दो
    if search:
        data = Employee.objects.filter(name__icontains=search)
    else:
        data = Employee.objects.all()

    return render(Request, "index.html", {'data': data})


def delete(Request,id):
    data=Employee.objects.get(id=id)
    if(data):
        data.delete()
        return redirect("/")

def addRecord(Request):
    if(Request.method=="POST"):
        e=Employee()
        e.name=Request.POST.get("name")
        e.email=Request.POST.get("email")
        e.phone=Request.POST.get("phone")
        e.salary=Request.POST.get("salary")
        e.city=Request.POST.get("city")
        e.state=Request.POST.get("state")
        e.save()
        return redirect("/")
    return render(Request,"add.html")


def updateRecord(Request,id):
    data=Employee.objects.get(id=id)
    if(Request.method=="POST"):
        data.name=Request.POST.get('name')
        data.email=Request.POST.get("email")
        data.phone=Request.POST.get("phone")
        data.salary=Request.POST.get("salary")
        data.city=Request.POST.get("city")
        data.state=Request.POST.get("state")
        data.save()
        return redirect("/")
    return render(Request,"update.html",{'data':data})
    