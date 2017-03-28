from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired
from wtforms import validators




class tenantForm(Form):
    tenant_name = StringField('Tenant Name', [validators.Regexp('^.*_TN$', message='Must Contain "_TN" at the end of the Tenant Name')])
    submit = SubmitField('Create a Tenant')


class bdForm(Form):
    tenant_name = StringField('Tenant name', validators=[DataRequired()])
    bd_name = StringField('BD name', validators=[DataRequired()])
    vrf_name = StringField('VRF name', validators=[DataRequired()])
    bd_subnet = StringField('BD subnet', validators=[DataRequired()])
    submit = SubmitField('Create Bridge Domain')


class aepForm(Form):
    aep_name = StringField('AEP name', [validators.Regexp('^.*_AEP$', message='Must Contain"_AEP" at the end of the name')])
    phy_name = StringField('PHY name', [validators.Regexp('^.*_PHY$', message='Must Contain"_PHY" at the end of the name')])
    submit = SubmitField('Create AEP')


class appForm(Form):
    app_name = StringField('APP name', [validators.Regexp('^.*_AP$', message='Must Contain"_AP" at the end of the name')])
    tenant_name = StringField('Tenant Name', [validators.Regexp('^.*_TN$', message='Must Contain "_TN" at the end of the Tenant Name')])
    submit = SubmitField('Create APP')
    

class epgForm(Form):
    app_name = StringField('AEP name', [validators.Regexp('^.*_AEP$', message='Must Contain"_AEP" at the end of the name')])
    tenant_name = StringField('Tenant Name', [validators.Regexp('^.*_TN$', message='Must Contain "_TN" at the end of the Tenant Name')])
    bd_name = StringField('BD name', validators=[DataRequired()])
    epg_name = StringField('AEP name', [validators.Regexp('^.*_EPG$', message='Must Contain"_EPG" at the end of the name')])




class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password')
    submit = SubmitField('Sign Up')


class dmvpnForm(Form):
    dev_prod = StringField('Prod of Dev', validators=[DataRequired()])
    data_center = StringField('Data Center')
    service_type = StringField('In/Out of Service')
    submit = SubmitField('Submit')

class csvForm(Form):
    csv_file = FileField(u'CSV File')
    submit = SubmitField('Upload CSV')

