from rest_framework import serializers
from .models import Employee


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class EmployeeSerializer(serializers.ModelSerializer):
    subordinates = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['fullname', 'position', 'entry_date', 'salary', 'subordinates']
