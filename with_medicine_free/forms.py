from django import forms
from .models import Free_board, Free_Comment

class Free_board_Form(forms.ModelForm):
    class Meta:
        model = Free_board
        fields = ['title', 'body', 'image']
        
class Free_board_CommentForm(forms.ModelForm):
    class Meta:
        model = Free_Comment
        fields = ['b_text']
        labels = {
            'b_text' : '작성할 댓글' ,
        }