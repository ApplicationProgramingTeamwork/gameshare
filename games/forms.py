from django import forms
from .models import BoardGame

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'genre', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }