from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    # def clean_name(self):
    #     data = self.cleaned_data.get('title')
    #     if "D" in data:
    #         return data
    #     else:
    #         raise forms.ValidationError('imię musi zawierać D')