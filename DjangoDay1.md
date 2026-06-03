# MVT Design Pattern
- M :- Its stands for models which is reponsible to handle database related code 
- V :- Its stands for Views which is reponsible to handle all the logics suchs as Validation<br>    Authentication,  Authorization,registration and login
- T :- Its is responsible html related code 

# Step To Display a django project 
1. Create a new Django Project
2. Go inside New Created Project 
3. Create a new application
4. Create a view in views.py 
- view is a nothing a function in django which accept resquest and send back the respond
- Check Syntex in views.py
5. Call the view inside a path of urls.py
- Check in url.py

# Step To connect html page 
1. Create template folder in root level directory and create html page which whatever your choice
2. Configure about templates in setting.py
- In setting.py inside TEMPLATES  add :- 'DIR':[os.path.join(BASE_DIR,"templates")]
3. Use Render Function to render the html page 
- Render is a function is used to merge both static and dynamic data present in html<br> 
and give a single output .Check in view.py