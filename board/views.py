from django.shortcuts import render, redirect
from alice_user.models import AliceUser
from .models import Board
from .forms import BoardForm
# Create your views here.


def boardDetail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boardDetail.html', {'board': board})


def boardwrite(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            aliceUser = AliceUser.objects.get(pk=user_id)


            
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = aliceUser
            board.save

            return redirect('/board/list')

    else:
        form = BoardForm()
        
    return render(request, 'boardwrite.html', {'form': form})


def boardlist(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'boardlist.html', {'boards': boards})