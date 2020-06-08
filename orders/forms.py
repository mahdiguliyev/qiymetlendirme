from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['company_name', 'order_name','subcategory_name','order_law_decision', 'order_deptor', 'order_claimant', 'order_information', 'order_document', 'order_keep_date_location','order_mobile']
        widget={"order_document" : forms.ClearableFileInput(attrs={'multiple': True})} 