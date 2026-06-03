# Static Files 

- These are files which doesnt change and its data is constant 
- These files can be anythings images , css , Js

## Step to Work on Static file
- 1. Create a static folder ,in root level directory of a project 
-   inside it create subfolder like images,css,js
struture
```
staic/
│
├── css/
├── images/
├── js/

```
- 2. Stores the images .jpeg , .jpg or .png extention
- 3. Configure about static folder in setting.py as follow 
syntex
```
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static")
]

```
To display image in html used the below syntx
```
{% mainfoldername 'subfoldername/imageaname with extension'%}

example:-
<img src="{% static 'images/deadpool.jpg'%}">
```
- 4. HTNL page not recognize the above syntx 
To make it understand we need to load about static in the beggning og html page
```
{% load static %}
```
- 5. To use external css , Create inside css sub_folder and link that inside head tag of html page
```
href="{% static 'css/mystyle.css'%}"
```
