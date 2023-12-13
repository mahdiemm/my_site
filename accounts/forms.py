from typing import Any
from django import forms
from .models import CustomUser,Subject,Teacher
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
            'class':'form-control'
        })
        self.fields["phone_number"].widget.attrs.update({
            'class':'form-control'
        })
        self.fields["fullname"].widget.attrs.update({
            'class':'form-control'
        })
        self.fields["password1"].widget.attrs.update({
            'class':'form-control'
        })
        self.fields["password2"].widget.attrs.update({
            'class':'form-control'
        })
        self.fields["rules"].widget.attrs.update({
            'class':'form-check-input'
        })



    email = forms.EmailField(max_length=255)
    phone_number = PhoneNumberField(
        required=False,
        widget=PhoneNumberPrefixWidget(initial="IR")
    )
    fullname = forms.CharField(max_length=255)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    rules = forms.BooleanField()

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email","phone_number", "fullname","password1", "password2","rules",)


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'class':'form-control'
        })
        self.fields["password"].widget.attrs.update({
            'class':'form-control'
        })
    

    username = forms.EmailField(max_length=255)
        

    password = forms.CharField(widget=forms.PasswordInput)
    class Meta(AuthenticationForm):
        model = CustomUser
        fields = ("username","password","phone_number")


class TeacherRequest(forms.ModelForm):
    TYPE = (
      ('TEACHER', 'teacher'),
      ('ORGANIZATIONS', 'organ'),
    )
    PAYMENT = (
      ('ZARIN', 'Zarin'),
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["account"].widget.attrs.update({
            'class':'form-select'
        })
        self.fields["documents"].widget.attrs.update({
            'class':'form-control'
        })
        self.fields["payment"].widget.attrs.update({
            'class':'form-select'
        })
        self.fields["identity"].widget.attrs.update({
            'class':'form-control'
        }) 
        self.fields["body"].widget.attrs.update({
            'class':'form-control'
        })

    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    account = forms.ChoiceField(choices=TYPE)
    documents = forms.FileField()
    payment =forms.ChoiceField(choices=PAYMENT)
    identity = forms.FileField()
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Teacher
        fields = ("subject", "account", "payment", "identity", "documents", "body")






 
        