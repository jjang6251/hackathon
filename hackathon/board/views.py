from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
# from .forms import BoardWriteForm
from django import forms
from board.models import Board
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from datetime import date, datetime, timedelta


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

# 상세보기 기능
def board_detail(request, pk):
    board = get_object_or_404(Board, id=pk)
    board.view_count += 1
    board.save()
    context = {
        'board_image' : board.board_image,
        'title' : board.title,
        'board_nickname' : board.board_nickname,
        'board_location_si' : board.board_location_si,
        'board_location_gu' : board.board_location_gu,
        'board_location_dong' : board.board_location_dong,
        'board_number' : board.board_number,
        'board_content' : board.board_content,
        'money' : board.money,
        'board_write_dttm' : board.board_write_dttm,
        'view_count' : board.view_count,
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
        board.board_image = request.FILES.get("board_image", board.board_image)
        board.board_nickname = request.POST.get("board_nickname", board.board_nickname)
        board.title = request.POST.get("title", board.title)
        board.money = request.POST.get("money", board.money)
        board.board_content = request.POST.get("board_content", board.board_content)
        board.board_location_si = request.POST.get("board_location_si", board.board_location_si)
        board.board_location_gu = request.POST.get("board_location_gu", board.board_location_gu)
        board.board_location_dong = request.POST.get("board_location_dong", board.board_location_dong)
        board.board_number = request.POST.get("board_number", board.board_number)
        board.save()
        return redirect("accounts:board:board_list")


    return render(request, 'board/board_modify.html')