from django import forms
from django.contrib.auth.models import User
from . models import Profile,Post,Comments

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(
                        attrs = {'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(
                        attrs = {'placeholder':'Confirm Password...'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password

class Login_Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
    					attrs={'placeholder':'Eneter valid username'}))
    password = forms.CharField(widget=forms.PasswordInput(
    					attrs={'placeholder':'Enter vallid password....'}))


class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =('user',) 


class User_form(forms.ModelForm):
        class Meta:
            model = User
            fields = (
                'username',
                'first_name',
                'last_name',
                'email',
            )

class PostForm(forms.ModelForm):
    class Meta:
        model   = Post
        fields  =(
            'title',
            'content',
            'status',
            )

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'status',
            
        )
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)







