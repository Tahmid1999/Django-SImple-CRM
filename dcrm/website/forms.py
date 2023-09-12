from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import  forms
from  .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Name'}),
        help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
        help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}),
        help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')    
        
        

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}),
        label=""
    )
    
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
        label=""
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}),
        label=""
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Address", "class": "form-control"}),
        label=""
    )

    city = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "City", "class": "form-control"}),
        label=""
    )

    state = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "State", "class": "form-control"}),
        label=""
    )

    zipcode = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Zipcode", "class": "form-control"}),
        label=""
    )
    
    class Meta:
        model = Record
        exclude = ("user",)
    