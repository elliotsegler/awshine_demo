from django import forms

class FeebackForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Email'}))
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control rating', 'min':1,'max':5,'step':1,'data-size':"lg"}))
    feedbackText = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Feedback'}))
