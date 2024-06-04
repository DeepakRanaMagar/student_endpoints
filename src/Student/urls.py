from django.urls import path
from .views import StudentCrud, StudentView
from . import views

urlpatterns = [
    # path("", StudentView.as_view(), name='student-create'),
    path("", views.index, name='homepage'),
    path("login",views.login, name="login"),
    path("logout",views.logout, name="logout"),

    path('<int:pk>/', StudentView.as_view(), name='student-update'),
    path('add',StudentCrud.create,name="student-add"),
    path('view',StudentCrud.student_list,name="student-list"),
    path('update',StudentCrud.update,name="student-crud"),
    path('edit/<id>',StudentCrud.edit, name="id"),
    path('delete/<std_id>',StudentCrud.delete, name="std_id"),


]
