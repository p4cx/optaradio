from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddStationForm(FlaskForm):
    station_name = StringField('Station name', validators=[DataRequired()])
    station_url = StringField('Stream url', validators=[DataRequired()])
    station_desc = StringField('Description', validators=[DataRequired()])
    station_cover = FileField('Cover', validators=[FileAllowed(['png'], '*.png only!')])
    station_country = StringField('Country', validators=[DataRequired()])

    submit = SubmitField('Add station')




