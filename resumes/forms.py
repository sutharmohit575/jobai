from django import forms
from .models import Resume

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Senior Developer Resume'}),
        }
