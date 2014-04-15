from rest_framework import serializers
from admissions.models import Institution


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('institute_id', 'name', 'address', 'city', 'state', 'start_class_level', 'end_class_level',)



