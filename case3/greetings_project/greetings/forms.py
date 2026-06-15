from django import forms
from .models import UserName

class NameForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        # Аттрибут required ставим в False, чтобы браузер не блокировал отправку формы с пустым значением
        # и чтобы можно было отругать пользователя за невведенное поле нашими словами :)
        self.fields['name'].required = False

    class Meta:
        model = UserName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше имя...'
            })
        }
        labels = {
            'name': ''
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError('Это поле обязательно для заполнения.')
        return name.strip()
