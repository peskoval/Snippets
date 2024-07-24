from django.forms import ModelForm, TextInput, Textarea, ValidationError
from MainApp.models import Snippet


# Описание возможностей по настройке форм
# https://docs.djangoproject.com/en/dev/ref/forms/widgets/#django.forms.Widget.attrs

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'status']
        labels = {'name': '', 'lang': "", "code": "", "status": ""}
        widgets = {
          'name': TextInput(attrs={"class":"form-control", "style":'max-width: 300px;', 'placeholder': 'Название сниппета'}),
          'code': Textarea(attrs={
              'placeholder': 'Код сниппета', 
              'rows': 5, 
              'class': 'input-large', 
              'style': 'width: 50% !important; resize: vertical !important;'
              }),
        }