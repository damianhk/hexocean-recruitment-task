from django.db import models


class UserTier(models.Model):
    TIER_CHOICES = (
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Enterprise', 'Enterprise'),
    )
    name = models.CharField(max_length=50, choices=TIER_CHOICES)

class Image(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tier = models.ForeignKey(UserTier, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
