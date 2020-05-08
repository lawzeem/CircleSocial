from django import forms
from .models import ChatMessage


class ComposeForm(forms.Form):
     class Meta:
        model = ChatMessage
        fields = {'message',}