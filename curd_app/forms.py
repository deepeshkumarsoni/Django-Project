from django import forms

class ProductCreateForm(forms.Form):

    P_id=forms.IntegerField(
        label='Enter Product Id :',
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Product ID'
            }
        )

    )
    P_name = forms.CharField(
        label='Enter Product Name :',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Product Name'
            }
        )

    )
    P_cost = forms.IntegerField(
        label='Enter Product Cost :',
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Product Cost'
            }
        )

    )
    P_color = forms.CharField(
        label='Enter Product Color',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Product Color'
            }
        )

    )
    P_class = forms.CharField(
        label='Enter Product Class',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Product Class'
            }
        )

    )

class ProductUpdateForm(forms.Form):

    P_id = forms.IntegerField(
        label='Enter Product Id',
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Product ID'
            }
        )

    )
    P_cost = forms.IntegerField(
        label='Enter Product Cost :',
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Product Cost'
            }
        )

    )

class ProductDeleteForm(forms.Form):

    P_id = forms.IntegerField(
        label='Enter Product Id',
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Your Product ID'
            }
        )

    )