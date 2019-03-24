from django.db import models
from django.contrib.auth.models import User

FILTER_COURSES = (
    ('IOT', 'IOT'),
    ('Ethical Hacking', 'Ethical Hacking'),
    ('Augmented Reality', 'Augmented Reality'),
    ('Machine Learning', 'Machine Learning'),
)


# Create your models here.
class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    course = models.CharField(max_length=30, choices=FILTER_COURSES)
    score = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + str(self.score)
