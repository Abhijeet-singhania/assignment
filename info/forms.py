from django import forms
from . import models

class CreateItem(forms.ModelForm):
    class Meta:
        model = models.Items
        fields = ('name', 'quantity', 'status','date',)
        # fields = "__all__"  