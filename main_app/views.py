from django.shortcuts import render

from .models import Knot
# knots = [
#   {
#     'name': 'bowline', 
#     'types': ('loop', 'basic'), 'description': 'Makes a loop in the end of a rope'
#     },
#   {
#     'name': 'figure eight', 
#     'types': ('stopper',), 'description': 'A good stopper knot'
#     },
# ]

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