# from django.shortcuts import render,redirect
# from .models import Member
# from .forms import MemberForm
# from django.contrib import messages

# def home(request):
#     all_members=Member.objects.all
#     return render(request, 'home.html' ,{'all':all_members})

# def join(request):
#     if(request.method =="POST"):
#         form=MemberForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#         messages.success(request,('Your form has been submitted successfull!'))
#         return render(request, 'base.html',{})
#         # return redirect('base')

#     else:
#         return  render(request , 'join.html' ,{})
  

from django.shortcuts import render,redirect
from .models import Member
# from .forms import MemberForm
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv 


# from .forms import MemberForm

def home(request):
    all_members=Member.objects.all
    return render(request, 'home.html' ,{'all':all_members})

def join(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST" :
        
        q1 = request.POST['Fname1']
        q2 = request.POST['Fname2']
        q3 = request.POST['Lname1']
        q4 = request.POST['Lname2']
        q5 = request.POST['Roll1']
        q6 = request.POST['Roll2']
        q7 = request.POST['Phone1']
        q8 = request.POST['Phone2']
        q9 = request.POST['Email1']
        q10 = request.POST['Email2']
        q11 = request.POST['Q1']
        q12 = request.POST['Q2']
        
        data=Member.objects.create(
       Fname1=q1,
        Fname2=q2,
        Lname1=q3,
        Lname2=q4,
        Roll1=q5,
        Roll2=q6,
        Phone1=q7,
        Phone2=q8,
        Email1=q9,
        Email2=q10,
        Q1=q11,
        Q2=q12,




        )
        data.save()
        # with open('participants.csv', 'a' ,newline='') as csvfile:
        #             spamwriter=csv.writer(csvfile, delimiter='',
        #                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #             data1=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17]  

        #             spamwriter.writerow(data1)      


        with open('participants1.csv', 'a', newline='') as csvfile:                 
                    spamwriter= csv.writer(csvfile)
                    data1=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]
    
                    spamwriter.writerow(data1)

        # create a form instance and populate it with data from the request:
        messages.success(request,('Your form has been submitted successfull!'))
        return render(request, 'thanks.html',{})

     
    return render(request, 'join.html',{})   
