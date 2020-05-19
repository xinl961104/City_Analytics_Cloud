from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


FEATURES = [
    ('Melbourne Inner', 'Melbourne Inner'),
    ('Melbourne Inner West', 'Melbourne Inner West'),
    ('Melbourne Inner East', 'Melbourne Inner East'),
    ('Melbourne Inner South', 'Melbourne Inner South'),
    ('Melbourne North East', 'Melbourne North East'),
    ('Melbourne North West', 'Melbourne North West'),
    ('Melbourne Outer East', 'Melbourne Outer East'),
    ('Melbourne South East', 'Melbourne South East'),
    ('Melbourne West', 'Melbourne West'),
    ('Mornington Peninsula', 'Mornington Peninsula'),
]


# The feature, date range selection form in template - home.html
# This form includes three fields - feature, start date, end date
class featureSelectionForm(forms.Form):
    features = forms.ChoiceField(
        choices=FEATURES,
    )

