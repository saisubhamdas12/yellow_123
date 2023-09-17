from django.db import models

# Create your models here.
class Maid(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)


class AvailabilitySlot(models.Model):
        maid = models.ForeignKey(Maid, on_delete=models.CASCADE)
        start_time = models.DateTimeField()
        end_time = models.DateTimeField()

class Review(models.Model):
        maid = models.ForeignKey(Maid, on_delete=models.CASCADE)
        rating = models.DecimalField(max_digits=3, decimal_places=1)
        comment = models.TextField()

class booking_detail(models.Model):
        maid = models.ForeignKey(Maid, on_delete=models.CASCADE)
        user_name=models.CharField(max_length=100)
        phone_number=models.CharField(max_length=10)
        address=models.CharField(max_length=100)