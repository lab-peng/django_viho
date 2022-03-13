from django import forms
from .models import ProjectFile

class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['file',]
        widgets = {
            'file': forms.ClearableFileInput(attrs={
                                        'multiple': True,
                                        'id': 'file-upload',
                                        'style': 'display:none;'
                                        })
                }