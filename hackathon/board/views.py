from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
# from .forms import BoardWriteForm
from django import forms
from board.models import Board
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from .forms import *
from .models import *
from accounts.models import *



# 목록 리스트
@login_required
def board_list(request):
    if not request.user.is_authenticated:
        return redirect('accounts:afterlogin')
    board_lists = Board.objects.all() # Board 전체 데이터 조회
    #board_list = Board.objects.filter(writer=request.user) # Board.writer가 현재 로그인인 것 조회
    context = {
        'board_lists': board_lists,
    }
    return render(request, 'board/board_list.html', context)

# 글쓰기 기능(Create)
#  # 로그인 했을 때만 가능한 것
def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:board:board_list')
        else:
            form = BoardForm()

    return render(request, 'board/board_write.html')
    
# 업데이트 기능(Update)
def board_update(request, id):
    board = Board.objects.get(id=id)
    if request.method == 'GET':
        context = { 'board' : board }
        return render(request,'board/board_write.html', context)
    elif request.method == 'POST':
        pass

def board_detail(request):
    board_detail = Board.objects.all() # Board 전체 데이터 조회
    context = {
        'board_detail': board_detail,
    }
    return render(request, 'board/board_detail.html', context)


# # @login_message_required
# def board_delete(request, id):
#     board = Board.objects.get(id=id)
#     if board.writer == request.user or request.user.level == '0':
#         board.delete()
#         messages.success(request, "삭제되었습니다.")
#         return redirect('/notice/')
#     else:
#         messages.error(request, "본인 게시글이 아닙니다.")
#         return redirect('/notice/'+str(id))

def board_modify(request, pk):
    board = get_object_or_404(Board, id=pk)

    if request.method == 'POST':
        board.board_image = request.FILES["board_image"]
        board.board_nickname = request.POST["board_nickname"]
        board.title = request.POST["title"]
        board.money = request.POST["money"]
        board.board_content = request.POST["board_content"]
        board.board_location = request.POST["board_location"]
        board.board_number = request.POST["board_number"]
        board.save()
        return redirect("accounts:board:board_list")


    return render(request, 'board/board_write.html')