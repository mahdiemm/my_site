from django import forms
from .models import CourseComment, AnswerCourseComment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['body'].widget.attrs.update({
            'class':'form-control',
        })
    class Meta:
        model = CourseComment
        fields = ('body',)


class AnswerCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['answer'].widget.attrs.update({
            'class':'form-control',
        })
    class Meta:
        model = AnswerCourseComment
        fields = ('answer',)