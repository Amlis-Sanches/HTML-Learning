# How to use Django
To start we are needing to install Django through pip. In my case I needed to create a Virtual python to run this code and then install Django. The guide to this is [[virtual python environment]] and explains how to install the virtual environment and run Django.

## Creating a project
to create a project we need to run #CMD and navigate to the appropriate folder we want to create our project using `cd` command. Then use the following command `django-admin startproject PROJECT_NAME`. 

> [!tip]
> If you cannot run Django on your regular python, create a [[virtual python environment]] and run Django on that for its commands through the activate file within #CMD . 

Now you will notice that there is a few files that were created
- Manage.py: This is the file we will use to run command within this project. 
- settings.py: Contains important configuration settings for us. Comes preloaded
- urls.py: A table of contents for us that contains all the urls within this project.

## Run Django
once a project has been created we are ready to test run a server or our project. This is done within the #CMD window:
1. Open project folder with `cd` to access Manage.py
2. run the server with `python manage.py runserver`
3. Copy the URL that is linked to your computer.
4. To quit use `CONTROL-C`

Congratulations, you created and ran your first Django project. 

# Creating Apps


