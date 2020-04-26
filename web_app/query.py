from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class QueryForm(FlaskForm):
    postcode = StringField('Postcode', 
    validators=[DataRequired(), Length(min=4, max=4)])

    submit = SubmitField('Submit')        
 