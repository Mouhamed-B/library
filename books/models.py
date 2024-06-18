from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    STATUSES = [
        ('AVAILABLE','AVAILABLE'),
        ('CHECKED_OUT','CHECKED_OUT')
    ]

    title = models.CharField(max_length=127, blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    image = models.URLField(blank=False, null=False)
    checked_out_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, default=None)

    @property
    def status(self):
        return 'Available' if self.checked_out_by is None else 'Checked Out'