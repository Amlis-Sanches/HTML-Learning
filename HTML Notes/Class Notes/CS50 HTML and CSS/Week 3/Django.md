# How to use Django
To start we are needing to install Django through pip. In my case I needed to create a Virtual python to run this code and then install Django. The guide to this is [[virtual python environment]] and explains how to install the virtual environment and run Django.

## Creating a project
to create a project we need to run #CMD and navigate to the appropriate folder we want to create our project using `cd` command. Then use the following command `django-admin startproject PROJECT_NAME`. 

> [!tip]
> If you cannot run Django on your regular python, create a [[virtual python environment]] and run Django on that for its commands through the activate file within #CMD . 

Now you will notice that there is a few files that were created
- Manage.py: This is the file we will use to run command within this project. 
- project folder
	- `__init__.py` : your importing file for the manage.py
	- settings.py: Contains important configuration settings for us. Comes preloaded
	- urls.py: A table of contents for us that contains all the urls within this project.
	- asgi.py: 
	- wshi.py:

## Run Django
once a project has been created we are ready to test run a server or our project. This is done within the #CMD window:
1. Open project folder with `cd` to access Manage.py
2. run the server with `python manage.py runserver`
3. Copy the URL that is linked to your computer.
4. To quit use `CONTROL-C`

> [!tip]
> You need to be in the folder that the manage.py is in. If you want to quickly open cmd into that folder, using the folder window replace the path with cmd and press enter. 

Congratulations, you created and ran your first Django project. Though you still need to access the page. That is done through the IP address: 127.0.0.1 with a port number of 8000. Copy the link it provides and open it into a browser. This is an address only you can access.

# Creating a App
Django is able to take multiple different projects and separate them into multiple apps. We will create a basic hello world app and to create any app, make sure your server is off, you are also in the correct file path where manage.py is and type `python manage.py startapp hello`. Now instead of your project directory you will also have hello directory holding:
- Migrations folder
- `__init__.py`: for your importing
- admin.py
- apps.py
- models.py
- tests.py
- views.py: This is the file that describes what the user sees when the access the hello page.

But we aren't done yet. We also need to install the app into the main project folder. Access the main project folder (in our case lecture3) and open the settings.py. Scroll down until you see `INSTALLED_APPS = []`. Here you need to install the hello app. so add to the list of strings `hello,`. don't forget the comma. Now hello is an installed app for this website.

## Creating a Page
### Views
When starting the coding for a page we need to start by creating a function. In our case our example is going to be index. When creating any function for a page we need to add the variable `request`. We can add others but we will start with request. to display an item we need to import the `HttpResponse`. Then using this new class we can have the function return `HttpResponse("Hello, World")`. 

``` python
from django.http import HttpResponse
from django.shorcuts import render

#Create your views here.
def index(request):
	return HttpResponse("Hello, World!")
```

But now we need to tell the app when to return this response?

### Apps URL's
We can call urls within multiple areas but in our case we will create urls within our apps folder `hello`. In urls we need to import `django.urls import path & from . import views` and we need to describe a variable `urlspatterns = []`. Here need to describe the path to the index function we just created by adding to the list `path("", views.index, name="index"`


### Add urls to main url folder. 
The last step you need to do is add this url to the main projects folder url.py file. Here we will add to the list variable `path('hello/',include("hello.urls"))` and import `from django.urls import include, path`. Now when you run the server you with /hello you have a page with hello world message.

## Creating Additional Pages
When creating additional pages for example Brian and David, we follow the same steps for [[#Views]] and [[#Apps URL's]]. Here we create a new function and then add it to the url path. Creating a new function with a new name and new string descriptions. But in the urls.py list variable instead of leaving the string blank we will add a name. This will create an additional page where hello/brian will run the function brian. 

```python
def brian(request):
    return HttpResponse("Hello Brian")

def david(request):
    return HttpResponse("Hello David")
```

```python
    path("brian", views.brian, name="brian"),
    path("david",views.david, name="david"),
```

## Creating Specialized Function Patterns 
But creating a page for multiple names becomes tedious, in this case we can create path converters. Where the function we create will take an additional parameter to change the name for that file and then the path will have a new name we will create a variable `"<str:name>"`. Saying that any string that comes off of hello/str will run a custom function to direct the message to the attributes within the url path.

```python
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
```

```python
path("<str:name>", views.greet, name="greet"),
```

## Templates
When creating HTML parts into your page you use the `HttpResponse()` method. Unfortunately this is going to be a lot of HTML into one string. Instead you can use html files to help create your response. This is done through the render command that is imported `from django.shortcuts import render`. Then change the function to render a HTML file. 

```python
def index(request):
    return render(request, "hello/index.html")
```

Then we need to create a new folder path to what we indicated above. Within the hello app create the following path hello/templates/hello. The reason we create an additional folder is because we indicated it in the string above when calling the file. Then create index.html. Here we are going to follow the same steps we have done before with [[HTML]]. 
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>
```

But HTML is a template language and not really a programming language, so we don't have functions, variables or classes. Using Django, we can add these abilities when creating a HTML file. 

### Django Variables
Using render we are going to add a additional variable to give additional context. In our case we are using name as the variable name and it will be capitalized. Using the name we can use `{{}}` to tell Django that a variable is located here. In our case we will use `{{ name }}`.
```python
def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
```

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        <h1>Hello , {{ name }}!</h1>
    </body>
</html>
```

In a whole we are creating a function called greet, linking the function with path inside a list and then using HTML as a template for our webpage. 

### Django If Statements
Though say we wanted to submit a true or false statement into the HTML code to dictate what we are going to see. Let's make something simple where we want to know if its new years or not. we create a new [[#Creating a App| App]], then linking the [[#Apps URL's]] and [[#Add urls to main url folder.| URLS]]. Then we can create the new function within the view.py file to determine if today is the first month and first day.
```python
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
```
This will send a TRUE or FALSE response. Then in the HTML template we can create a if statement by using `{%%}`.  Where with a bool value you can determine the heading that is displayed. Then when opening the view of the HTML page you will only see the h1 that passed. when closing logic you need to put the {% endif %}.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Is it New Year's?</title>
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```

### CSS in Django
### Create a Static file
First thing to do is to create a new .css file for you to load into the HTML. Using Django you need to create a new file path within your application folder. Using newyear as an example we need to create a new folder path and file as follow: `static/newyear/styles.css`. The reason for putting these files into a folder called static is that these files don't change and won't when programming the webpage.

```css
h1 {
    font-family: sans-serif;
    font-size: 90px;
    text-align: center;
}
```

### Pull CSS into HTML
Once the file is created you can pull the CSS file with Django by loading the static library at the beginning of the HTML code with `{% load static %}`. and then just like we learned with [[CSS|CSS3]] we need to load the specific CSS file. But this time we are we are going to modify the link to the css file with `<link href="{% static "newyear/styles.css" %}" rel="stylesheet">`
This not only means that this will load the URLs for the static file but if the file is moved you will automatically have the HTML files updated. 

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Is it New Year's?</title>
        <link href="{% static "newyear/styles.css" %}" rel="stylesheet">
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```

