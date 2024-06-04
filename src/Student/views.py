
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from Student.forms import StudentForm
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Student

# Create your views here.
class StudentView(APIView):
    '''
        Handles the Request to the POST()
    '''    
    permission_classes = [AllowAny,]
    
    def post(self, request):
        '''
            Handles the POST() request
        '''
        
        data = request.data
        # print(data)

        serializer = StudentSerializer(data=data)
        # print(serializer)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {
                        "Your data is succesfully posted."
                    }, status=status.HTTP_201_CREATED
                )
            except Exception as e: 
                return Response(
                    {
                        "Error": str(e)
                    }, status=status.HTTP_401_UNAUTHORIZED
                )
        
        return Response({
                "Detail": serializer.errors
            }, status=status.HTTP_401_UNAUTHORIZED
        )
    
    def put(self, request, pk):
        '''
            Handles the PUT() request, to update the instance of the Student Model
        '''
        data = request.data
        print(data)
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=data)
        print(serializer)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {
                        "Your record is updated Successfully."
                    }
                )
            except Exception as e:
                return Response(str(e))
        return Response({
                "Detail": serializer.errors
            }, status=status.HTTP_401_UNAUTHORIZED
        )

class StudentCrud():
    def superuser_required(user):
        return user.is_superuser

    @user_passes_test(superuser_required)
    def update(request):
        students=Student.objects.all()
        return render(request, "update.html",{'students':students})

    def create(request):
        if request.method=="POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/students/view')
        form=StudentForm()
        return render(request,"createform.html",{'form':form})
    
    def student_list(request):
        students=Student.objects.all()

        return render(request,"student_list.html",{'students':students})
    
    @user_passes_test(superuser_required)
    def edit(request,id):
        student=Student.objects.filter(id=id).first()
        if(request.method=="POST"):
            student.name=request.POST.get("name")
            student.age=request.POST.get("age")
            student.address=request.POST.get("address")
            student.grade=request.POST.get("grade")
            student.major=request.POST.get("major")
            student.save()
            return redirect('/students/view')
        return render(request, "edit.html",{'student':student})
    
    @user_passes_test(superuser_required)
    def delete(request,std_id):
        student=Student.objects.filter(id=std_id)
        student.delete()
        return redirect('/students/view')
    

def index(request):
    return render(request,"home.html")

def login(request):
    auth.logout(request)
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/students')
        else:
            messages.info(request,"Invalid credentials !!")
    return render(request, "log.html")

def logout(request):
    auth.logout(request)
    return redirect('/students')