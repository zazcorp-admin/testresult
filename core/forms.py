from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = '__all__'
        labels = {
            'title': 'Title',
            'fat': 'FAT(3.5% to 4.3%)',
            'snf': 'SNF(7.8 to 8.4)',
            'urea': 'Urea(0.0% to 0.5%)',
            'starch': 'Starch(0.0% to 0.5%)',
            'detergent': 'Detergent(0.0% to 0.5%)',
            'antibiotic': 'Antibiotic(0.0% to 0.5%)',
            'acidity': 'Acidity(0.0v/v-68.0v/v)',
            'caustic_soda': 'Caustic Soda(0.0% to 0.5%)',
            'desc': 'Description',

        }

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'fat': forms.TextInput(attrs={'class':'form-control'}),
            'snf': forms.TextInput(attrs={'class':'form-control'}),
            'urea': forms.TextInput(attrs={'class':'form-control'}),
            'starch': forms.TextInput(attrs={'class':'form-control'}),
            'detergent': forms.TextInput(attrs={'class':'form-control'}),
            'antibiotic': forms.TextInput(attrs={'class':'form-control'}),
            'acidity': forms.TextInput(attrs={'class':'form-control'}),
            'caustic_soda': forms.TextInput(attrs={'class':'form-control'}),
        }


class TermsForm(forms.ModelForm):
    terms = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = TermsAndCondition
        fields = '__all__'

