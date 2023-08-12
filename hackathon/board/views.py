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
    if request.method == 'GET':
        return render(request, 'board/board_write.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        title = request.POST.get('title')
        user_nickname = request.POST.get('user_nickname')
        user_location = request.POST.get('user_location')
        user_ph_number = request.POST.get('user_ph_number'),
        print(image)
        print(content)
        print(title)
        print(user_nickname)
        print(user_location)
        print(user_ph_number)

        # 데이터 생성
        Board.objects.create(
            image=image,
            content=content,
            title=title,
            user_nickname=user_nickname,
            user_location=user_location,
            user_ph_number=user_ph_number,
            # writer = request.user
        )
        return redirect('accounts:homepage')
    
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