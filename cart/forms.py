# -*- coding : utf-8 -*-
# coding: utf-8

from django import forms


#PRODUCT_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    #quantity = forms.TypedChoiceField(label='数量', choices=PRODUCT_QUANTITY_CHOICE, coerce=int)
    quantity = forms.IntegerField(label='数量', initial=1, min_value=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
