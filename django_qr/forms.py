from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(max_length=50, 
        label="Restaurant Form",
        widget=forms.TextInput(attrs={
            'class': 'form-control', # class is an attribute with form-control class of bootstrap
            'placeholder' : 'Enter Restaurant Name: '
        })
        )

    url = forms.URLField(max_length=200, 
        label="Menu URL",
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder': 'Enter the URL for your online menu : '
        })
        )
