from django.shortcuts import render
from django.views.generic import View
from operation.forms import RegistrationForm
from operation.forms import VehicleForm
from operation.forms import BmrForm
from operation.forms import AppointmentForm
from operation.forms import BmiForm
from operation.forms import MilageForm,CalorieForm


# Create your views here.


class AdditionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'add.html')
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get('num1')

        num2=form_data.get('num2')

        result=int(num1)+int(num2)

        print(result)

        data={
            'output':result
        }

        return render(request,'add.html',data)
    
#subtration
class SubtractionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'sub.html')
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get('num1')

        num2=form_data.get('num2')

        result=int(num1)-int(num2)

        print(result)

        data={
            'output':result
        }

        return render(request,'sub.html',data)    
    
#multiplication
class MultiplicationView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'multiply.html')
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get('num1')

        num2=form_data.get('num2')

        result=int(num1)*int(num2)

        print(result)

        data={
            'output':result
        }

        return render(request,'multiply.html',data)    
#Division Operation
class DivisionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'div.html')
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get('num1')

        num2=form_data.get('num2')

        result=int(num1)/int(num2)

        print(result)

        data={
            'output':result
        }

        return render(request,'div.html',data)        
    
#Signup form   
class SignUpView(View):

    def get(self,request,*ags,**kwargs):

        

        form_instance=RegistrationForm()
        context={
            "form":form_instance
        }

        return render(request,"register.html",context)



#vehicle form
class VehicleAddView(View):

    def get(self,request,*args,**kwargs):

        form_instance=VehicleForm()

        context={
            'form':form_instance
        }

        return render(request,'vehicle.html',context)
    
#bmr
class BmrView(View):
    def get(self,request,*args,**kwargs):
        form_instance=BmrForm()

        context={
            'form':form_instance
        }   
        return render(request,'bmr.html',context)

#application form
class AppointmentView(View):
    def get(self,request,*args,**kwargs):
        form_instance=AppointmentForm()

        context={
            'form':form_instance
        }     
        return render(request,'appointment.html',context)  
    
#bmi
class BmiView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BmiForm()

        context={
            'form':form_instance
        }   
        
        return render(request,'bmi.html',context)
    
    def post(self,request,*args,**kwargs):

        #step 1 extract form data
        form_data=request.POST

        #step2 initialize form_instance with form_data
        form_instance=BmiForm(form_data)

        #step 3 chk form valid or not
        if form_instance.is_valid():

            data=form_instance.cleaned_data #{'weight': 53, 'height': 151}

            height=data.get("height")

            weight=data.get("weight")

            BMI=weight/(height/100)**2

            print(BMI)
        
        return render(request,"bmi.html",{'form':form_instance,"result":BMI})
    
#milage
class MilageView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MilageForm()

        context={
            "form":form_instance
        }   

        return render(request,"milage.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=MilageForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            distance=data.get("distance")

            consumption=data.get("consumption")

            Milage=distance/consumption

            print(Milage)

        return render(request,"milage.html",{'form':form_instance,'result':Milage})


#calorie
class CalorieView(View):

    def get(self,request,*args,**kwargs):

        form_instance=CalorieForm()

        context={
            'form':form_instance
        }

        return render(request,'calorie.html',context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=CalorieForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data #{'weight': 43, 'height': 125, 'age': 14, 'gender': 'male', 'activity': '1.2'}

            print(data)

            weight=data.get("weight")

            height=data.get("height")

            age=data.get('age')

            gender=data.get("gender")

            activity=data.get("activity")

            if gender=='male':

                BMR=10*weight+6.25*height-5*age+5

            else:

                 BMR=10*weight+6.25*height-5*age-161 

            calorie=BMR*float(activity)      

        return render(request,'calorie.html',{'form':form_instance,'bmr':BMR,'calorie':calorie})    
    







    
     
    
    
