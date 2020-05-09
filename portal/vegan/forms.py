from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


FEATURES = [
    ('Ausinner', 'Ausinner'),
    ('Phone', 'Phone'),
    ('Beacons', 'Beacons'),
    ('Bemyeyes', 'Bemyeyes'),
    ('Books', 'Books'),
    ('Live Radio', 'Live Radio'),
    ('Magnifer', 'Magnifer'),
    ('News', 'News'),
    ('Podcast', 'Podcast'),
    ('Timers', 'Timers'),
]


# The feature, date range selection form in template - home.html
# This form includes three fields - feature, start date, end date
class featureSelectionForm(forms.Form):
    features = forms.ChoiceField(
        choices=FEATURES,
    )

