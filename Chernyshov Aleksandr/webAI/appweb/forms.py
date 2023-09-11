from django import forms

class PostForm(forms.ModelForm):
    pass
    #name = forms.CharField(label='Названиее поста',
    #                       widget=forms.TextInput(attrs={"placeholder": 'Название', 'class': 'form-control'})
    #                       )

    #text = forms.CharField(label="Текст поста",
    #                       widget=forms.TextInput(attrs={"placeholder": 'Текст поста', 'class': 'form-control'})
    #                       )

    #class Meta:  # прописывается модель данных(из model.py) для заполнения которой нам нужна форма.
    #    model = Post
    #    fields = '__all__'  # говорит о том что форма предложит заполнить все поля которые есть в модели