# DJANGO TEMPLATES LANGUAGE OR JINJA PATTERN
- It is a patterns or tags used handle dynamic data which is coming to html page 
- Its has own syntex and rules to handle the data 
- Its used for to handle simple and complex data like text,integer,list,images,external files and 
- to import and inheritent the data .
```bash
{{ }} -> To handle simple data

{% %} -> To handle the complex data

syntex:- 
1. To use for loop {% %} {% end %}
{% for varname in collectiontype %}
    # Statement 1
    # Statement 2
{% end %}

2. To use if condition
{% if cond%}

remaining





```
Notes:- 
- 1. In this whenever we started the block we need to end that block mannualy
- 2. If you using any mathematical operator we need to maintain the space before and after the    operator

# CREF TOKEN 
- 1. Its stand for cross side requested forgery , it act like a middleware 
- 2. Its Help to avoid the displaying the input data entered in html page in url configuration
- 3. Its is used inside the form when the form method is post 
### Example
```bash
<form action="url path names " method="POST">
{% %}

</form>

GET :- It is a method of http protocol used to get the imformation which is already present 
POST :- It is a method which is used to add the new imformation 

```

