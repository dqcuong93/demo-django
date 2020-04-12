from django import forms
from . import models


class BookInputForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'title',
            'content',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
