from django.db import models
from django.urls import reverse

# Create your models here.
class Knot(models.Model):
  name = models.CharField(max_length=100)
  # type = models.CharField(max_length=50)
  description = models.CharField(max_length=250)


  def __str__(self):
    return self.name
  

  def get_absolute_url(self):
    return reverse('detail', kwargs={'knot_id': self.id})


# data for knot types model
KNOT_TYPES = (
 ('b', 'bend'),
 ('h', 'hitch'),
 ('l', 'loop'),
 ('o', 'other'),
 ('s', 'stopper'),
)

class Type(models.Model):
  type = models.CharField(
    max_length=1,
    choices=KNOT_TYPES
    )