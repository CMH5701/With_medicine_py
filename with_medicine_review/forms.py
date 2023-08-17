from django import forms
from .models import Review_board, Review_Comment

class Review_board_Form(forms.ModelForm):
    class Meta:
        model = Review_board
        fields = ['title', 'body', 'image']
        
class Review_board_CommentForm(forms.ModelForm):
    class Meta:
        model = Review_Comment
        fields = ['b_text']
        labels = {
            'b_text' : '작성할 댓글' ,
        }