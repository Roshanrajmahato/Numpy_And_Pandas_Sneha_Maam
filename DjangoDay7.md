# Django 

- 1. It is a external mo                  which help in giving addition styling to the Django Form.
- 2. Follow the Step To Impliment it in the Project
   - Install Below Module 
```bash
    pip install django-crispy-forms

    pip install crispy-bootstrap5
   ```
- 3. Mention the Module name in list of install app on setting.py 
setting.py
```
INSTALLED_APPS = [

    'crispy_forms',
    "crispy_bootstrap5"
]

```
Configure its templates  as follows in setting.py itself
```
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

```

- 4. Load its Crispy Tag in html page at the begning of html page 
```
{% load crispy_forms_tags %}
```

- 5. To apply crispy forms functionality for the existing form for all the fields at once use the below sytax
```
{{ form.filedName | crispy_field }}
``

- To give the Fuctionality to each field we need to the same sytam


