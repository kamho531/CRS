from django import forms
from .models import Customer



# create add record form
class AddCustomerForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}))
    last_name = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}))
    email = forms.EmailField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}))
    phone = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Phone No. xxx-xxx-xxxx", "class":"form-control"}))
    address = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}))
    city = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}))
    province = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Province", "class":"form-control"}))
    postalcode = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Postal Code", "class":"form-control"}))

    class Meta:
        model = Customer
        exclude = ("user",)
