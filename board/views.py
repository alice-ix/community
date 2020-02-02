from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from alice_user.models import AliceUser
from tag.models import Tag
from .models import Board
from .forms import BoardForm
# Create your views here.


def boardDetail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'boardDetail.html', {'board': board})


def boardwrite(request):
    if not request.session.get('user'):
        return redirect('/alice_user/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            aliceUser = AliceUser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = aliceUser
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()
        
    return render(request, 'boardwrite.html', {'form': form})


def boardlist(request):
    
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 2)

    boards = paginator.get_page(page)
    return render(request, 'boardlist.html', {'boards': boards})