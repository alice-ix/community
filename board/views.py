from django.shortcuts import render
from .models import Board
# Create your views here.
def boardlist(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'boardlist.html', {'boards': boards})