from django import forms
from mirror.models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['color_palettes', 'novel_atmo', 'novel_genre', 'patient']