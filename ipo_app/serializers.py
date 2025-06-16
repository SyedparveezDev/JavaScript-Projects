from rest_framework import serializers
from .models import IPO


class IPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPO
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class IPOListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPO
        fields = ('id', 'company_name', 'company_logo', 'issue_size', 'price_band', 
                 'open_date', 'close_date', 'status', 'lot_size')
