import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings')
import django
django.setup()
from random import *
from faker import Faker
from modelapp3.models import Student
fakegen=Faker()

def phonenumgen():
    d1 = randint(6,9)
    num = ''+str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fsno=fakegen.random_int(min=1,max=1000)
        fsname=fakegen.name()
        froll=fakegen.random_int(min=1211,max=4132)
        femail=fakegen.email()
        fdob=fakegen.date()
        fmark=fakegen.random_int(min=1,max=600)
        fnumber=phonenumgen()
        faddress=fakegen.address()
        Student.objects.get_or_create(sno=fsno,sname=fsname,sroll=froll,email=femail,dob=fdob,mark=fmark,
        phone=fnumber,address=faddress)

n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully....')    


