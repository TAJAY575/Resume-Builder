# creating a resume builder with flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ResumeForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email')
    phonenumber = StringField('Phone Number', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    jobtitle= StringField('Job Title')
    company = StringField('Company')
    schoolname = StringField('School Name')
    degree = StringField('Degree')
    fieldofstudy = StringField('Field Of Study')
    start_date = StringField('Start Date')
    end_date = StringField('End Date')
    skill = StringField('Skill #')
    intrest = StringField('Intrests')
    submit = SubmitField('Submit')

