from django.forms import ModelForm
from django import forms
from .models import Batch


class BatchForm(ModelForm):
    # extend upon Batch's meta class
    end_date = forms.DateField(input_formats=['%d-%m-%Y'])
    class Meta:
        model = Batch 
        #fields = ['name','style','start_date','end_date','score','comment']
        fields = '__all__'
