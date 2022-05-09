from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    my_category = SelectField('Category', choices=[('Marketing','Marketing'),('Promotional','Promotional'),('Scholarship','Scholarship')],validators=[InputRequired()])
    my_pitches = TextAreaField('Enter Pitch', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave Your Comments Below..', validators=[InputRequired()])
    submit = SubmitField('Submit Comments')
    
class BioForm(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')