# Django Model 
- Models is consider as a individual table present in the database
- In Dajngo Models will be created with the help the ORM(Oject Relationl Mapper) Module , It helps us to create the object to our model class and then integrate it with the database (Either Inbuilt or External Database)

## Step to Create Django Models
- 1. Create a class in models.py and convert that class into models by inherating models.Model class.
- 2. Create Total No number of field is required in models inside a model class 
- 3. In this Models is treated as table and fields is treated as columns.
- 4. For each data thier is a specific field , we need to use the same filed.
Example:-
```
id=models.IntegerField()
degree=models.CharField(max_length=20)
age=models.PositiveIntegerField()
phone=models.BigIntegerField()
email=models.EmailsField()
photo=models.ImageField()
DOB=modles.DateField()
```
- 5. After Creating the the models mention application name in list of install apps in setting.py
```md
INSATLLED_APPS=[
    'aapname'
]
```
- 6. Run the Commands to keep track the changes and to reflect the changes 
- makemigration :- it is command to keep track the changes what is happening in models.py ,
Changes like :- 
creating a new models , 
adding new fiels ,
changing name of the field , 
deleting existing forld
 ```bash
python manage.py makemigrations
 ```
- migrate :- It is a command which help to reflect the changes from models to database(admin)
```bash
python manage.py migrate
```

- 7. To login for internal database (Admin Panel)
Enter The cammand
```bash
python manage.py createsuperuser

```
Make :-
USERNAME
PASSWORDS



- 8. To register model in admin panel ,Follow the below syntex In 
admin.py
example:-
```
import appname.models from classname

admin.site.register(classname)
```

Notes:- 
If Any changes happen in models.py , run the above two command repeatedly 
Run makemigration untill we get ,no changes detected and migrate Untill no migration is applied

If Any changes happened in models.py ,we need to run the above two command untill, migration is successfull.

- 9. Run the Django Development Server

Start the development server.

## Command

```bash
python manage.py runserver
```