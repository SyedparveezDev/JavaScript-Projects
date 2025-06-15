from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date, timedelta
from .models import IPO


class IPOModelTest(TestCase):
    """Test cases for IPO model."""
    
    def setUp(self):
        """Set up test data."""
        self.ipo_data = {
            'company_name': 'Test Company',
            'issue_size': 1000.00,
            'price_band': '100-120',
            'open_date': date.today() + timedelta(days=1),
            'close_date': date.today() + timedelta(days=5),
            'status': 'upcoming',
            'lot_size': 100,
            'description': 'Test IPO description'
        }
    
    def test_ipo_creation(self):
        """Test IPO model creation."""
        ipo = IPO.objects.create(**self.ipo_data)
        self.assertEqual(ipo.company_name, 'Test Company')
        self.assertEqual(ipo.status, 'upcoming')
        self.assertTrue(ipo.is_upcoming)
        self.assertFalse(ipo.is_ongoing)
        self.assertFalse(ipo.is_listed)
    
    def test_ipo_str_method(self):
        """Test IPO string representation."""
        ipo = IPO.objects.create(**self.ipo_data)
        self.assertEqual(str(ipo), 'Test Company')


class IPOViewTest(TestCase):
    """Test cases for IPO views."""
    
    def setUp(self):
        """Set up test data and client."""
        self.client = Client()
        self.ipo = IPO.objects.create(
            company_name='Test Company',
            issue_size=1000.00,
            price_band='100-120',
            open_date=date.today() + timedelta(days=1),
            close_date=date.today() + timedelta(days=5),
            status='upcoming',
            lot_size=100,
            description='Test IPO description'
        )
    
    def test_home_view(self):
        """Test home page view."""
        response = self.client.get(reverse('ipo_app:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'IPO Investment Platform')
    
    def test_ipo_list_view(self):
        """Test IPO list view."""
        response = self.client.get(reverse('ipo_app:ipo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Company')
    
    def test_ipo_detail_view(self):
        """Test IPO detail view."""
        response = self.client.get(reverse('ipo_app:ipo_detail', args=[self.ipo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Company')
    
    def test_ipo_list_filter(self):
        """Test IPO list filtering."""
        response = self.client.get(reverse('ipo_app:ipo_list') + '?status=upcoming')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Company')
    
    def test_ipo_search(self):
        """Test IPO search functionality."""
        response = self.client.get(reverse('ipo_app:ipo_list') + '?search=Test')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Company')


class IPOAPITest(TestCase):
    """Test cases for IPO API."""
    
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.ipo = IPO.objects.create(
            company_name='API Test Company',
            issue_size=2000.00,
            price_band='200-240',
            open_date=date.today() + timedelta(days=2),
            close_date=date.today() + timedelta(days=6),
            status='ongoing',
            lot_size=50,
            description='API Test IPO description'
        )
    
    def test_api_overview(self):
        """Test API overview endpoint."""
        response = self.client.get(reverse('ipo_app:api_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_api_ipo_list(self):
        """Test API IPO list endpoint."""
        response = self.client.get(reverse('ipo_app:api_ipo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_api_ipo_detail(self):
        """Test API IPO detail endpoint."""
        response = self.client.get(reverse('ipo_app:api_ipo_detail', args=[self.ipo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
