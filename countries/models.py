from django.db import models

class Country(models.Model):
    """Country model."""
    
    iso_code = models.CharField(max_length=2,unique=True)
    name = models.CharField(max_length=255,unique=True)

    class Meta:
        ordering = ('iso_code',)

    def __str__(self):
        return self.name