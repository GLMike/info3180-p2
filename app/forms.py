from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, DataRequired

class ModelForm(FlaskForm):
    
    model = StringField('Car Model', 
                                validators=[DataRequired()])
    model = StringField('Car Make', 
                                validators=[DataRequired()])

    submit = SubmitField("Search")
