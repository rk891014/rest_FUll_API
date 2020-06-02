from rest_framework import serializers
from . models import employees


class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=employees
        fields=('firstname','lastname','emp_id','id','image')
        # fields=('_all_')