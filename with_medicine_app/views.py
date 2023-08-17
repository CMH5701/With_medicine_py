from django.shortcuts import render
from with_medicine_free.models import Free_board
from with_medicine_review.models import Review_board
from django.db.models import Q

# Create your views here.

def main(request):
    free_boards = Free_board.objects.order_by('-pub_date')[:3]
    review_boards = Review_board.objects.order_by('-pub_date')[:3]
    return render(request, 'main.html', {'free_boards': free_boards, 'review_boards':review_boards})

def main_search(request):
    free_board = Free_board.objects.all().order_by('-id')
    review_board = Review_board.objects.all().order_by('-id')
    
    q = request.POST.get('q', "")
    
    if q:
        free_board = free_board.filter(Q (title__icontains=q) | Q (body__icontains=q))
        review_board = review_board.filter(Q (title__icontains=q) | Q (body__icontains=q))
        return render(request, 'main_search.html', {'free_board':free_board, 'review_board':review_board, 'q':q})
    
    else:
        return render(request, 'main_search.html', {'free_board':free_board, 'review_board':review_board})