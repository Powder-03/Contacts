from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ['id', 'owner', 'country_code', 'firstname', 'last_name', 'phone_number', 'contact_picture', 'is_favourite']