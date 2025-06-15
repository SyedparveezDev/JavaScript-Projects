from django.db import models
from django.core.validators import MinValueValidator


class IPO(models.Model):
    IPO_STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('listed', 'Listed'),
    ]
    
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    issue_size = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    price_band = models.CharField(max_length=50)
    open_date = models.DateField()
    close_date = models.DateField()
    listing_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=IPO_STATUS_CHOICES, default='upcoming')
    rhp_document = models.FileField(upload_to='documents/rhp/', blank=True, null=True)
    drhp_document = models.FileField(upload_to='documents/drhp/', blank=True, null=True)
    description = models.TextField(blank=True)
    lot_size = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'IPO'
        verbose_name_plural = 'IPOs'
    
    def __str__(self):
        return self.company_name
    
    @property
    def is_upcoming(self):
        return self.status == 'upcoming'
    
    @property
    def is_ongoing(self):
        return self.status == 'ongoing'
    
    @property
    def is_listed(self):
        return self.status == 'listed'
