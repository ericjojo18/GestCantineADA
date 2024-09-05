from django.db import models

class Plat(models.Model):
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats"