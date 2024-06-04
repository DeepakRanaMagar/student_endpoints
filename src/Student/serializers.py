from rest_framework import serializers
from .models import Student
from django.db import transaction


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
        
    @transaction.atomic
    def create(self, validated_data):
        '''
            Handles the creation of Student instances
        '''
        
        try:
            
            student = Student.objects.create(**validated_data)
            print(student)
            return student
        
        except Exception as e:
            raise e
    
    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            instance.name = validated_data.get('name', instance.name)
            instance.age = validated_data.get('age', instance.age)
            instance.address = validated_data.get('address', instance.address)
            instance.grade = validated_data.get('grade', instance.grade)
            instance.major = validated_data.get('major', instance.major)

            instance.save()
            return instance
        except Exception as e:
            raise serializers.ValidationError(
                {
                    "details": str(e)
                }
            )
