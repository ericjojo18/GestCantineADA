from django.db import models
from cantine.models.helpers.date_time_model import DateTimeModel
from cantine.models.plat_model import Plat

class Menu(DateTimeModel):
    plat = models.OneToOneField(Plat, on_delete=models.CASCADE)
    
    def __str__(self):
        return f" {self.plat.name}"

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"