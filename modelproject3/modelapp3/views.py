from django.shortcuts import render
from modelapp3.models import Student
def get(request):
    data=Student.objects.all()
    rec={"datav":data}
    return render(request,'Pages/student.html',rec)
    
