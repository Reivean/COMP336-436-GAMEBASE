from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField, SelectField, HiddenField, Form
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flaskDemo import db
from flaskDemo.models import Reservation, User1, Item, User1_type, Item_type, Publisher, Location, Language, Author
#from flaskDemo.models import User, Department, getDepartment, getDepartmentFactory, Employee, Project, Works_On, Reservation, User, Item
from wtforms.fields.html5 import DateField
from flask_table import Table, Col, LinkCol

# ssns = Department.query.with_entities(Department.mgr_ssn).distinct()
# emp = Employee.query.with_entities(Employee.ssn, Employee.fname,Employee.lname)
# proj = Project.query.with_entities(Project.pnumber, Project.pname)
user1typeid = User1_type.query.with_entities(User1_type.User1_type_id, User1_type.Name)
userid = User1.query.with_entities(User1.User_Id, User1.UName)
itemid = Item.query.with_entities(Item.Item_Id, Item.Title)
publisherid = Publisher.query.with_entities(Publisher.Publisher_Id)
locationid = Location.query.with_entities(Location.Rack_Id)
languageid = Language.query.with_entities(Language.Language_Id, Language.Language_Name)
itemtypeid = Item_type.query.with_entities(Item_type.Item_type_id, Item_type.Type_name)
authorid = Author.query.with_entities(Author.Author_Id, Author.FirstName, Author.LastName)


#### query to get usertype id and name from table

# results=list()
# for row in ssns:
#     rowDict=row._asdict()
#     results.append(rowDict)
# myChoices = [(row['mgr_ssn'],row['mgr_ssn']) for row in results]

# results=list()
# for row in emp:
#     rowDict=row._asdict()
#     results.append(rowDict)
# myChoices3 = [(row['fname'] + row['lname'], row['ssn']) for row in results]

results=list()
for row in itemid:
     rowDict=row._asdict()
     results.append(rowDict)
myChoices7 = [(row['Item_Id'], row['Title']) for row in results]


results=list()
for row in userid:
     rowDict=row._asdict()
     results.append(rowDict)
myChoices6 = [(row['User_Id'], row['UName']) for row in results]


# results=list()
# for row in proj:
#     rowDict=row._asdict()
#     results.append(rowDict)
# myChoices4 = [(row['pname'], row['pnumber']) for row in results]

#### create strcture

results=list()
for row in user1typeid:
    rowDict=row._asdict()
    results.append(rowDict)
mychoices5 = [(row['User1_type_id'], row['Name']) for row in results]

#Emmanuel For Add Form below
results=list()
for row in publisherid:
     rowDict=row._asdict()
     results.append(rowDict)
myChoices9 = [(row['Publisher_Id'], row['Publisher_Id']) for row in results]

results=list()
for row in languageid:
     rowDict=row._asdict()
     results.append(rowDict)
myChoices10 = [(row['Language_Id'], row['Language_Name']) for row in results]

results=list()
for row in locationid:
     rowDict=row._asdict()
     results.append(rowDict)
myChoices11 = [(row['Rack_Id'], row['Rack_Id']) for row in results]

results=list()
for row in itemtypeid:
     rowDict=row._asdict()
     results.append(rowDict)
myChoices12 = [(row['Item_type_id'], row['Type_name']) for row in results]

results=list()
for row in authorid:
     rowDict=row._asdict()
     results.append(rowDict)
myChoices13 = [(row['Author_Id'], row['FirstName'] + " " + row['LastName']) for row in results]

#Emmanuel For Add Form Above


regex1='^((((19|20)(([02468][048])|([13579][26]))-02-29))|((20[0-9][0-9])|(19[0-9][0-9]))-((((0[1-9])'
regex2='|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))$'
regex=regex1 + regex2


class RegistrationForm(FlaskForm):
    # username = StringField('Username',
    #                        validators=[DataRequired(), Length(min=2, max=20)])
    firstname = StringField('First Name',
                        validators=[DataRequired()])
    lastname = StringField('Last Name',
                            validators=[DataRequired()])

    uname = StringField('Username',
                        validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    address = StringField('Address',
                            validators=[DataRequired()])

    dateofbirth = DateField('DOB',
                                validators=[DataRequired()])

    user1typeid = SelectField("User's type", choices=mychoices5, coerce=int)

       #### user type drop down
    
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User1.query.filter_by(Email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

    
# class DeptUpdateForm(FlaskForm):

# #    dnumber=IntegerField('Department Number', validators=[DataRequired()])
#     dnumber = HiddenField("")

#     dname=StringField('Employee Name:', validators=[DataRequired(),Length(max=15)])
# #  Commented out using a text field, validated with a Regexp.  That also works, but a hassle to enter ssn.
# #    mgr_ssn = StringField("Manager's SSN", validators=[DataRequired(),Regexp('^(?!000|666)[0-8][0-9]{2}(?!00)[0-9]{2}(?!0000)[0-9]{4}$', message="Please enter 9 digits for a social security.")])

 #One of many ways to use SelectField or QuerySelectField.  Lots of issues using those fields!!
     #mgr_ssn = SelectField("Manager's SSN", choices=myChoices)  # myChoices defined at top
    
# # the regexp works, and even gives an error message
# #    mgr_start=DateField("Manager's Start Date:  yyyy-mm-dd",validators=[Regexp(regex)])
# #    mgr_start = DateField("Manager's Start Date")

# #    mgr_start=DateField("Manager's Start Date", format='%Y-%m-%d')
#     mgr_start = DateField("Manager's start date:", format='%Y-%m-%d')  # This is using the html5 date picker (imported)
#     submit = SubmitField('Update this department')


# # got rid of def validate_dnumber

#     def validate_dname(self, dname):    # apparently in the company DB, dname is specified as unique
#          dept = Department.query.filter_by(dname=dname.data).first()
#          if dept and (str(dept.dnumber) != str(self.dnumber.data)):
             # raise ValidationError('That department name is already being used. Please choose a different name.')


# class DeptForm(DeptUpdateForm):

#     dnumber=IntegerField('Department Number', validators=[DataRequired()])
#     submit = SubmitField('Add this department')

#     def validate_dnumber(self, dnumber):    #because dnumber is primary key and should be unique
#         dept = Department.query.filter_by(dnumber=dnumber.data).first()
#         if dept:
#             raise ValidationError('That department number is taken. Please choose a different one.')


#class assignvalidate(FlaskForm):

#    dnumber=IntegerField('Department Number', validators=[DataRequired()])
  #  dnumber = HiddenField("")

   # dname=StringField('Employee Name:', validators=[DataRequired(),Length(max=15)])
#  Commented out using a text field, validated with a Regexp.  That also works, but a hassle to enter ssn.
#    mgr_ssn = StringField("Manager's SSN", validators=[DataRequired(),Regexp('^(?!000|666)[0-8][0-9]{2}(?!00)[0-9]{2}(?!0000)[0-9]{4}$', message="Please enter 9 digits for a social security.")])

#  One of many ways to use SelectField or QuerySelectField.  Lots of issues using those fields!!
 #   essn = SelectField("Employee's SSN", choices=myChoices3)  # myChoices defined at top
  #  pno = SelectField("Project No", choices=myChoices4) 

class reservevalidate(FlaskForm):

    User_ID = SelectField("Username", choices=myChoices6 , coerce=int)
    Item_Id = SelectField("Item's Title", choices=myChoices7 , coerce=int)
    

# the regexp works, and even gives an error message
#    mgr_start=DateField("Manager's Start Date:  yyyy-mm-dd",validators=[Regexp(regex)])
#    mgr_start = DateField("Manager's Start Date")

#    mgr_start=DateField("Manager's Start Date", format='%Y-%m-%d')
 #   mgr_start = DateField("Manager's start date:", format='%Y-%m-%d')  # This is using the html5 date picker (imported)
   # submit = SubmitField('Update this Relation')

class Reserveform(reservevalidate):

    # User_ID=SelectField('User1', validators=[DataRequired()])
    # Item_Id=SelectField('Item', validators=[DataRequired()])
    Due_Date = DateField("Due Date")
    submit = SubmitField('Add this relationship')

    def validate_User_ID_Item_Id(self, User_ID, Item_Id):
        User_ID = Reservation.query.filter_by(User_ID=User_ID.data,Item_Id=Item_Id.data).first()
        if User_ID:
            raise ValidationError('This relation is already reserved. Please choose a different one.')

   # essn=SelectField('Employee', validators=[DataRequired()])
   # pno=SelectField('Project', validators=[DataRequired()])
   # submit = SubmitField('Add this relationship')

    #def validate_essn_pno(self, essn, pno):    #because dnumber is primary key and should be unique
     #   essn = Works_On.query.filter_by(essn=essn.data,pno=pno.data).first()
      #  if essn:
       #     raise ValidationError('That employee is already assigned to the Project. Please choose a different one.')

#Reservation update Form - Made by Yanji
class ReserveUpdateForm(FlaskForm):
    Reservation_Id = HiddenField("")
    User_ID = SelectField("Update User's ID", choices=myChoices6, coerce=int)
    Item_Id = SelectField("Update Item's Title", choices=myChoices7, coerce=int)
    Due_Date = DateField("Update Due Date")
    submit = SubmitField('Update your reservation')
#End of the code - Made by Yanji
       
#Search form code -Ted
class ItemSearchForm(Form):
    choices = [("Title", "Title"),
               ("Author", "Author"),
               ("Publisher", "Publisher"),
               ("Keyword", "Keyword")]
    select = SelectField("Search for Item:", choices=choices)
    search = StringField("")
#End of search form code -Ted

#Emmanuel's code for Add form below

class AddItemform(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    publisher = SelectField("Publisher:", choices=myChoices9)
    language = SelectField("Language:", choices=myChoices10)
    location = SelectField("Location:", choices=myChoices11)
    keyword = StringField('Keyword', validators=[DataRequired()])
    type = SelectField("Search Types:", choices=myChoices12)
    item = StringField("Item ID:", validators=[DataRequired()])
    author = SelectField('Author', choices=myChoices13)
    publication_date = DateField('Publication Date')
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))

    submit = SubmitField('Add this Item')


#Emmanuel's code for Add form above



