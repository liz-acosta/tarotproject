from django import forms

class SendTextForm(forms.Form):
    fields = ('phone_number',)
    phone_number = forms.CharField(label='Text my reading to me!', max_length=15, required=True)