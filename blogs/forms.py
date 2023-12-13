from django import forms
from .models import Comment, AnswerComment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['body'].widget.attrs.update({
            'class':'form-control',
        })
    class Meta:
        model = Comment
        fields = ('body',)


class AnswerCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['answer'].widget.attrs.update({
            'class':'form-control',
        })
    class Meta:
        model = AnswerComment
        fields = ('answer',)

