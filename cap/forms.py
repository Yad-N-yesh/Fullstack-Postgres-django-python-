from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = "__all__"

        widgets = {

            'first_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'last_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'age': forms.NumberInput(
                attrs={'class':'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class':'form-control'}
            ),

            'phone': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'department': forms.Select(
                attrs={'class':'form-select'}
            ),

            'course': forms.Select(
                attrs={'class':'form-select'}
            ),

        }