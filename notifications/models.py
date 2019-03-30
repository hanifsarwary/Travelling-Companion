from django.db import models
from UserHandling.models import Profile
# Create your models here.


class Notification(models.Model):
    notification_to = models.ForeignKey(Profile,on_delete=models.CASCADE)
    notfication_text = models.TextField(default=notification_to.__str__(),max_length=200)
    generation_time = models.TimeField(auto_now_add=True)
    generation_date = models.DateField(auto_now_add=True)
    notification_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.notfication_text