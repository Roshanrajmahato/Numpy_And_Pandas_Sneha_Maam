# Step To Connect External Database 
- 1. Install External module which helps us to connect django and mysql .
```bash
pip install mysqlclient
```

- 2. Mention the credential of external database in setting.py
Credentials :-
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',# django.db.backends.databasesoftware(mysql,postsql,sqlserver)
        'NAME': 'studentdb', # Database Name in mysql
        'USER':'root', # default name of mysql
        'PASSWORD':'root', # password of mysql
        'HOST':'localhost', # localhost name
        'PORT':'3306' # port no mysql is running
    }
}

```

 ```bash
python manage.py makemigrations
 ```
- migrate :- It is a command which help to reflect the changes from models to database(admin)
```md
python manage.py migrate
```
Notes:- 
- in external database is table is create with the help of applicationname_modelname
- It will accept application name convert everything lc,suffic with underscore and it will add model name ,everything in lowercase 

Example:-
```
studentapp_student
```
-----
# Django Form
- 1. It is a class which help us to quickly generate the HTML form , without using HTML Syntax
- 2. It contains specific field to accept specific data
- 3. It used in validation of a data and also supports custom validation
- 4. It helps in store the data , enter in html page in the database

## Step To Create Django Forms
- 1. Create forms.py module inside the application folder 
- 2. Create a form with the help of class by inhereting forms.FORM class belows to django module
Example:-
```md
from django import forms

class FormName(forms.Form):
    name=forms.CharField(max_length=200)
    age=forms.IntegerField()
    marks=forms.IntegerField()
    address=forms.CharField(max_length=200)

```
- 3. While creating the forms ,we need to used the field 
- 4. To display the form in display in html page need to create for form class inside a respective views.py of html page and render the object
Example :-
views.py
```md
from EmpApp.forms import FormName
# Create your views here.
def index(request): 
    form=FormName() # For Displaying only the form field from EmpApp.forms in FormName where it is # mention
    return render(request,"index.html",{'form':form})

```
Need To Display Form in index Page , Need To Create Object form class in index method view and render the dictionary 

- 5. Display the form field using jinja pattern as follow
```bash
<html>
<body>
 {{ form.as_p }}
</body>
</html>

as_p is used to display as a paragraph style
```

# Model Form  
It is class Belong to django module which help to connect between models(Database) and forms
It aslo help to save the data in database which is enter by the user which is enter in the html page 

## Step To Works on Model Form 
- 1. Create a model in models.py
- 2. Mention the credentials of external database in setting.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employeedb',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'3306'
    }
}
```

- 3. In forms.py Create a class and convert it into model forms by inheriting forms.ModelForm in Formclass
```
# from appName.models import modelName
from EmpModelApp.models import Employee
# Create your models here.
class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee # model=modelName # from appName.models import modelName 
        # fields="__all__" # For All Fields
        fields=['name','age','desg','salary','address','phone']

```
- 4. Mention the model which we need to connect for the existing form by giving its name and its respective fields inside the nested class called Meta . 

- 5. Logic Need To write in 
views.py
```
from django.shortcuts import render
from EmpApp.forms import FormName

# Create your views here.
def index(request): 
    form=FormName() # For Displaying only the form field from EmpApp.forms in FormName where it is mention,
    # Its used to display the fields in the html page

    if request.method =='POST': # After Summiting the form
        # It conform that user Enter The Data 
        form=FormName(request.POST) # Getting the Data from forms_field by method post or 
        # Used To Accept the data entered in the form field
        if form.is_valid():
            print("Validation Sucess")
            form.save()

    return render(request,"index.html",{'form':form})

```
index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FormModel</title>
</head>
<body>
    <h1>Employee Form</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="SAVE">
    </form>
</body>
</html>

```

