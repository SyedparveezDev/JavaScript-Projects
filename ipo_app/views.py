from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import IPO
from .serializers import IPOSerializer, IPOListSerializer


# Django views for web interface
def home(request):
    """Home page showing IPO listings"""
    upcoming_ipos = IPO.objects.filter(status='upcoming')[:6]
    ongoing_ipos = IPO.objects.filter(status='ongoing')[:6]
    listed_ipos = IPO.objects.filter(status='listed')[:6]
    
    context = {
        'upcoming_ipos': upcoming_ipos,
        'ongoing_ipos': ongoing_ipos,
        'listed_ipos': listed_ipos,
    }
    return render(request, 'ipo_app/home.html', context)


def ipo_list(request):
    """List all IPOs with filtering"""
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')
    
    ipos = IPO.objects.all()
    
    if status_filter:
        ipos = ipos.filter(status=status_filter)
    
    if search_query:
        ipos = ipos.filter(
            Q(company_name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    context = {
        'ipos': ipos,
        'status_filter': status_filter,
        'search_query': search_query,
        'status_choices': IPO.IPO_STATUS_CHOICES,
    }
    return render(request, 'ipo_app/ipo_list.html', context)


def ipo_detail(request, pk):
    """IPO detail page"""
    ipo = get_object_or_404(IPO, pk=pk)
    context = {'ipo': ipo}
    return render(request, 'ipo_app/ipo_detail.html', context)


# REST API views
class IPOListAPIView(generics.ListAPIView):
    """API view to list all IPOs"""
    queryset = IPO.objects.all()
    serializer_class = IPOListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['company_name', 'description']
    ordering_fields = ['open_date', 'close_date', 'issue_size']
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class IPODetailAPIView(generics.RetrieveAPIView):
    """API view to get IPO detail"""
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer


@api_view(['GET'])
def api_overview(request):
    """API overview endpoint"""
    api_urls = {
        'List IPOs': '/api/ipo/',
        'IPO Detail': '/api/ipo/<int:pk>/',
        'Admin Panel': '/admin/',
    }
    return Response(api_urls)
