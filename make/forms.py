from django import forms
from make.models import Make

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML
from crispy_forms.bootstrap import PrependedAppendedText


class MakeUser1Form(forms.ModelForm):
    first_name1 = forms.CharField(label='First Name')
    middle_name1 = forms.CharField(label='Middle Name')
    last_name1 = forms.CharField(label='Last Name')
    sid1 = forms.CharField(label='Student number')
    email1 = forms.CharField(label='Email address')
    phone1 = forms.CharField(label='Phone number number')
    school1 = forms.CharField(label='School')
    year_level1 = forms.CharField(label='Year level')
    course1 = forms.CharField(label='Course')
    id_pic1 = forms.ImageField(label='ID picture')


    class Meta:
        model = Make
        fields = [
            'first_name1',
            'middle_name1',
            'last_name1',
            'email1',
            'phone1',
            'sid1',
            'school1',
            'year_level1',
            'course1',
            'id_pic1',
        ]

class MakeUser2Form(forms.ModelForm):
    first_name2 = forms.CharField(required=False, label='First Name ')
    middle_name2 = forms.CharField(required=False, label='Middle Name ')
    last_name2 = forms.CharField(required=False, label='Last Name ')
    email2 = forms.CharField(required=False, label='Email address ')
    phone2 = forms.CharField(required=False, label='Phone number ')
    sid2 = forms.CharField(required=False, label='Student number ')
    school2 = forms.CharField(required=False, label='School ')
    year_level2 = forms.CharField(required=False, label='Year level ')
    course2 = forms.CharField(required=False, label='Course ')
    id_pic2 = forms.ImageField(required=False, label='ID picture ')

    class Meta:
        model = Make
        fields = [
            'first_name2',
            'middle_name2',
            'last_name2',
            'email2',
            'phone2',
            'sid2',
            'school2',
            'year_level2',
            'course2',
            'id_pic2',
        ]

class MakeAppForm(forms.ModelForm):
    app_name = forms.CharField(label='Mobile application name')
    app_market = forms.CharField(label='Target Market')
    concept = forms.CharField(max_length=1000, widget=forms.Textarea)
    class Meta:
        model =Make
        fields = [
            'app_name',
            'purpose',
            'app_market',
            'concept',
        ]
