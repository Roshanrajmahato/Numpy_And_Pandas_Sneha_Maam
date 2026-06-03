# 
1. For each html page created in templates ,need to create seperate views in views.py
2. When their is more then two html pages ,need to give the path in application urls
```bash
urlpatterns=[
    path('',views.index),
    path('contact',views.contact),
    path('about',views.about),
    path('profile',views.profile),
]
```
3. Include the application url in project url
```bash
urlpatterns = [
    path('',include('myapp.urls')),
    path('admin/', admin.site.urls),
]
```