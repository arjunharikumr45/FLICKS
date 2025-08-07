from django import forms
from .models import Payment1

# class SubscriptionForm(forms.ModelForm):
#     class Meta:
#         model = Subscription
#         fields = ['username', 'password', 'amount', 'cvv']
#         widgets = {
#             'password': forms.PasswordInput(),
#             'cvv': forms.TextInput(attrs={'maxlength': 4}),
#         }



# from .models import Payment1

# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment1
#         fields = ['username', 'password', 'card_number', 'cvv', 'amount', 'subscription_plan']
#         widgets = {
#             'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
#             'card_number': forms.TextInput(attrs={
#                 'readonly': 'readonly', 
#                 'value': '**** **** **** 1234'
#             }),
#             'cvv': forms.TextInput(attrs={'placeholder': 'CVV'}),
#             'amount': forms.NumberInput(attrs={'step': '0.01'}),
#             'subscription_plan': forms.Select(choices=[
#                 ('Basic', 'Basic'),
#                 ('Standard', 'Standard'),
#                 ('Premium', 'Premium')
#             ])
#         }



from django import forms
from .models import Payment1

class Payment1Form(forms.ModelForm):
    class Meta:
        model = Payment1
        fields = ['username', 'password', 'card_number', 'cvv', 'amount', 'subscription_plan']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'card_number': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'value': '**** **** **** 1234'
            }),
            'cvv': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'CVV', 'maxlength': '4'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}),
            'subscription_plan': forms.Select(choices=[
                ('Basic', 'Basic'),
                ('Standard', 'Standard'),
                ('Premium', 'Premium')
            ], attrs={'class': 'form-control'}),
        }
