from django import forms

class SearchForm(forms.Form): # forms.Form 클래스 상속
    search_query = forms.CharField(label='Search', max_length=100) 
    # 검색어 입력 필드, label로 폼 필드의 레이블 지정