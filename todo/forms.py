from django import forms
from .models import Post

class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'due_data', 'priority',)
        widgets = {
            'due_data': DateInput()
        }