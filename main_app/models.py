from django.db import models
from django.urls import reverse

# Create your models here.
# data for knot types model
KNOT_TYPES = (
 ('b', 'bend'),
 ('h', 'hitch'),
 ('l', 'loop'),
 ('o', 'other'),
 ('s', 'stopper'),
)

class TypeOfKnot(models.Model):
  type = models.CharField(
    max_length=1,
    choices=KNOT_TYPES,
    default=KNOT_TYPES[3][0],
    )

  def __str__(self):
    return f"{self.get_type_display()}"
  

class Knot(models.Model):
  name = models.CharField(max_length=100)
  # type = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  type = models.ForeignKey(
    TypeOfKnot,
    on_delete=models.CASCADE,
    )


  def __str__(self):
    return self.name
  

  def get_absolute_url(self):
    return reverse('detail', kwargs={'knot_id': self.id})

