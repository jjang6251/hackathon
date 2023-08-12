from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
# from .forms import BoardWriteForm
from django import forms
from board.models import Board
from django.contrib.auth.decorators import login_required


from .forms import *
from .models import *



# 목록 리스트
def board_list(request):
    board_lists = Board.objects.all() # Board 전체 데이터 조회
    #board_list = Board.objects.filter(writer=request.user) # Board.writer가 현재 로그인인 것 조회
    context = {
        'board_lists': board_lists,
    }
    return render(request, 'board/board_list.html', context)

# 글쓰기 기능(Create)
# @login_required # 로그인 했을 때만 가능한 것
def board_write(request):
    # if request.method == 'GET':
    #     return render(request, 'board/board_write.html')
    # else:
    #     board_nickname = request.POST.get('board_nickname')
    #     board_location = request.POST.get('board_loaction')
    #     board_image = request.FILES.get('board_image')
    #     board_content = request.POST.get('board_content')
    #     title = request.POST.get('title')
    #     print(board_image)
    #     print(board_content)
    #     print(board_nickname)
    #     print(board_location)
    #     print(title)

    #     # 데이터 생성
    #     Board.objects.create(
    #         board_image=board_image,
    #         board_content=board_content,
    #         title=title,
    #         board_nickname=board_nickname,
    #         board_location=board_location,
    #     )
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