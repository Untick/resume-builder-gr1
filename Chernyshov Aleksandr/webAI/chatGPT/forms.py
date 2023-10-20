from chatGPT.models import GPTAssistaintCV
from django import forms

class GPTAssistaintCV(forms.ModelForm):

    class Meta:  # прописывается модель данных(из model.py) для заполнения которой нам нужна форма.
        model = GPTAssistaintCV
        fields = '__all__'  # говорит о том что форма предложит заполнить все поля которые есть в модели

