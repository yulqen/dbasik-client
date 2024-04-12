from django import forms


class SubmitAPIForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV file')
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)

