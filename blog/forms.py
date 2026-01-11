from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='Заголовок поста', max_length=100 ,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control col-md-6', 'placeholder': 'Введите название поста'}
                           ))

    content = forms.CharField(label='Содержимое поста', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Наберите пост'}))



class PostEditForm(forms.Form):
    post_id = forms.IntegerField(widget=forms.NumberInput())
    title = forms.CharField(label='Заголовок поста', max_length=100 ,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control col-md-6'}
                           ))

    content = forms.CharField(label='Содержимое поста', widget=forms.Textarea(attrs={'class': 'form-control'}))