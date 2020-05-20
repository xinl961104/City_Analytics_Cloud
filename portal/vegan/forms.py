from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


# The feature, date range selection form in template - home.html
# This form includes three fields - feature, start date, end date


# The feature, date range selection form in template - home.html
# This form includes three fields - feature, start date, end date
class featureSelectionForm(forms.Form):
    MelbourneInner = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ), required=False)
    MelbourneInnerEast = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ),required=False)
    MelbourneInnerSouth = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }

    ),required=False)
    MelbourneNorthEast = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ),required=False)
    MelbourneNorthWest = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ),required=False)
    MelbourneOuterEast = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ),required=False)
    MelbourneSouthEast = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ), required=False)
    MelbourneWest = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ), required=False)
    MorningtonPeninsula = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ), required=False)
