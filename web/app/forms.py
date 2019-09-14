from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class StationForm(FlaskForm):
    station_name = StringField('Station name', validators=[DataRequired()])
    station_url = StringField('Stream url', validators=[DataRequired()])
    station_description = StringField('Description', validators=[DataRequired()])
    station_cover = FileField('Cover', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    station_country = StringField('Country', validators=[DataRequired()])

    submit = SubmitField('Add station')



