from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo, NumberRange, Length, InputRequired, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired
from datetime import date
#we are going to need some login form for another page so keep for now
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
#    remember_me = BooleanField('Remember Me')
#    submit = SubmitField('Sign In')
#    
#    

class SearchForm(FlaskForm):
    program = SelectField('Program', validators=[Optional()], coerce=int
        )
    reportType = SelectField("Report Type", choices=[(-1,''), (1, "Coding Error"), 
        (2, "Suggestion"), (3, "Documentation"), 
        (4, "Hardware"), (5, "Query")
        ], default='', validators=[Optional()], coerce=int
        )
    severity = SelectField("Severity", choices=[(-1,''), (3, "Minor"), 
        (2, "Serious"), 
        (1, "Fatal")], default='', validators=[Optional()], coerce=int
        )
    
    areaName = SelectField('Functional Area', validators=[Optional()]
        )
    assignedTo = SelectField('Assigned To', validators=[Optional()], coerce=int
        )    
    status = SelectField("Status", choices=[(-1,''), (1, "Open"), (2, "Closed")], default='', validators=[Optional()], coerce=int
        )
    priority = SelectField("Priority", choices=[(-1,''), (1, "Fix immediately"), 
        (2, "Fix as soon as possible"), (3, "Fix before next milestone"),
        (4, "Fix before release"), (5, "Fix if possible"), 
        (6, "Optional")], default='', validators=[Optional()], coerce=int
        )
    resolution = SelectField("Resolution", choices=[(-1,''), (1, "Pending"), (2, "Fixed"),
        (3, "Irreproducible"), (4, "Deferred"), (5, "As designed"),
        (6, "Withdrawn by reporter"), (7, "Need more info"),
        (8, "Disagree with suggestion"), (9, "Duplicate")], default='', 
        validators=[Optional()], coerce=int
        ) 
    reportedBy = SelectField('Reported By', validators=[Optional()], coerce=int
        )
    discoveredDate = DateField('Discovered Date', validators=[Optional()], default=''
        )       
    resolvedBy = SelectField("Resolved By", validators=[Optional()], coerce=int
        )


class BugReportForm(FlaskForm):
    program = SelectField('Program', validators=[InputRequired()], coerce=int
        )

    reportType = SelectField("Report Type", choices=[(1, "Coding Error"), 
        (2, "Design Issue"),
        (3, "Suggestion"), (4, "Documentation"), 
        (5, "Hardware"), (6, "Query")
        ], validators=[InputRequired()], coerce=int
        )
    severity = SelectField("Severity", choices=[(3, "Minor"), 
        (2, "Serious"), 
        (1, "Fatal")], validators=[InputRequired()], coerce=int
        )
    summary = TextAreaField("Summary", validators=[DataRequired(), Length(min=1, max=400)]
        )
    reproducable = BooleanField("Reproducable"
        )
    description = TextAreaField("Description", validators=[DataRequired(), Length(min=1, max=400)]
        )
    suggestedFix = TextAreaField("Description", validators=[Optional(), Length(min=1, max=400)]
        )
    reportedBy = SelectField('Reported By', validators=[InputRequired()], coerce=int
        )
    discoveredDate = DateField('Discovered Date', default=date.today
        )
    assignedTo = SelectField('Assigned To', validators=[Optional()], coerce=int
        )
    comments = TextAreaField("comments", validators=[Optional(), Length(min=1, max=400)]
        )
    status = SelectField("Status", choices=[(-1, ''), (1, "Open"), (2, "Closed")], validators=[Optional()], coerce=int
        )
    priority = SelectField("Priority", choices=[(-1, ''), (1, "Fix immediately"), 
        (2, "Fix as soon as possible"), (3, "Fix before next milestone"),
        (4, "Fix before release"), (5, "Fix if possible"), 
        (6, "Optional")], validators=[Optional()], coerce=int
        )
    resolution = SelectField("Resolution", choices=[(-1, ''),(1, "Pending"), (2, "Fixed"),
        (3, "Irreproducible"), (4, "Deferred"), (5, "As designed"),
        (6, "Withdrawn by reporter"), (7, "Need more info"),
        (8, "Disagree with suggestion"), (9, "Duplicate")],
        validators=[Optional()], coerce=int
        )
    resolutionVersion = IntegerField("Resolution Version",
        validators=[Optional(), NumberRange(1, 1000, "Resolution Version must be between 1 and 1000")]
        )
    resolvedBy = SelectField("Resolved By", validators=[Optional()], coerce=int
        )
    resolvedDate = DateField("Resolved Date", validators=[Optional()]
        )
    testedBy = SelectField("Tested By", validators=[Optional()], coerce=int
        )
    testedDate = DateField("Tested Date", validators=[Optional()]
        )
    deferred = BooleanField("Deferred"
        )


class EditForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(min=1, max=40)]
    )
    username = StringField(
        'username',
        validators=[DataRequired(), Length(min=1, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=1, max=40)]
    )
    userLevel = IntegerField('User Level',
        validators=[NumberRange(1, 4, "User Level must be between 1 and 4")]
    )
    

class RegisterForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(min=1, max=40)]
    )
    username = StringField(
        'username',
        validators=[DataRequired(), Length(min=1, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=1, max=40)]
    )
    userLevel = IntegerField('User Level',
        validators=[NumberRange(1, 4, "User Level must be between 1 and 4")]
    )
    

class addFuncAreaForm(FlaskForm):
    program = SelectField('Program', validators=[Optional()], coerce=int)
    area = StringField('Functional Area', validators=[DataRequired(), Length(min=1, max = 40)])
    

class editFuncAreaForm(FlaskForm):
    program = SelectField('Program', validators=[Optional()], coerce=int)
    area = StringField('Functional Area', validators=[DataRequired(), Length(min=1, max = 40)])


class addProgramForm(FlaskForm):
    name = StringField(
            'name', validators = [DataRequired(), Length(min=1, max=40)])
    version = IntegerField(
            'version', validators = [DataRequired()])
    releaseNumber = IntegerField(
            'releaseNumber', validators = [DataRequired()])
    description = StringField(
            'description', validators = [DataRequired(), Length(min=1, max=40)])
    

class ExportForm(FlaskForm):
    bugReport = BooleanField('Bug Report')
    employee = BooleanField('Employee')
    functionalArea = BooleanField('Functional Area')
    program = BooleanField('Program')
    attachment = BooleanField('Attachment')