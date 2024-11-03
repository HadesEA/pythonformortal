from django.db import models

# Create your models here.

class Expectation(models.Model):
    content = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    # Posible solución para que se cree una tabla nueva en la base de datos.
    class Meta:
        db_table = "home1_expectations"