from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Knot

# Create your views here.
def about(request):
  return render(request, 'about.html')


def home(request):
  return render(request, 'home.html')


def knots_index(request):
  knots = Knot.objects.all()
  return render(request, 'knots/index.html', {'knots': knots})

def knots_detail(request, knot_id):
  knot = Knot.objects.get(id=knot_id)
  return render(request, 'knots/detail.html', {'knot': knot })


# class-based views
class KnotCreate(CreateView):
  model = Knot
  fields = '__all__'


class KnotUpdate(UpdateView):
  model = Knot
  fields = '__all__'

class KnotDelete(DeleteView):
  model = Knot
  success_url = '/knots'