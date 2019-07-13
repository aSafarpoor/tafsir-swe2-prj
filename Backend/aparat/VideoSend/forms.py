from django import forms
from VideoSend import models


class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Document
        fields = ('description', 'document' )
