Todo app
 ---
 613.Going From Idea To App
 ----
 Step 1 : Decide features
 User should be able to perform the following tasks:
  1 . Add/save
  the action user would perform:
  on the left hand side, we have the actions which the user performs and on the right hand side we actually have those things which we need to go ahead and do in Django
  1 enter a url on the browser -> write Url patterns
  2 Visits a page which contains a from  -> Create a template with a form
  3 enter task data and click submit -> A view which handles the POST request and a model which saves the data.

  2 . View
  3 . Update
  4 . Remove
 Step 2 : break features into model-view-templates
 step-3 : create models,views, templates, URL patterns in that order.

step-4 : if you want to go ahead and design the update or delete features inside your application,
-----
614. Installing Virtual environments:-
----
So what the virtual environments do is that they actually provide you with a virtual space for your project wherein you could go ahead and download any sort of application package or any
software which you want which won't interfere with the other software's which are installed on your computer.
 virtual environment is sort of like an isolated room, which you can use on your computer, which does not affect other installations on your machine.

 major advantages of using a virtual environment is that you could go ahead and install:
 -- multiple Django versions.
 --those two environments to test out your Django application.
 --provides a lot of flexibility

 install virtual environment on your computer, be it Windows or Mac, you need to go:-

 - pip install virtual env
  on windows go to the dir env/scripts
 whenever you want to activate the environment:-
 .\activate hit, enter
 whenever you want to deactivate the environment:-
  .\deactivate hit, enter

-----
615. Setting Up The Project
-----
Entire todoappis  project and myapp is simply a single application in entire website
to install the django in cmd
 - pip install django
create Django project:
- django-admin startproject todoapp
we want to create an application:
- django-admin startapp myapp

-----
616. Creating Model
----
we need to do here is that once you have created the models, you have to make migrations,
But even before you make migrations, you first need to go ahead and make sure that
you have added your my app into your settings.py file or else the migrations are not going to work.
simply go ahead and type in my app in the installed apps directory of the settings.py
We have added the app name here, we are now free to go ahead and make migrations.it will create the model called as task.
   -- python manage.py makemigrations

once you have made the migrations, you then need to type
 -- python3 manage.py migrate and hit enter.
all the migrations have been applied and a new model which is called as task

we have successfully completed the first feature or the first feature implementation of adding a task model

need to go ahead and log in into your admin site now in order to log in into your admin site,
order to create a super user, type  -- Python Manage.py createsuperuser.
giving usrname: admin
give dummy mail:----
password : Admin123
Superuser created successfully. run server
login :http://127.0.0.1:8000/admin/

need to go ahead and register those models into the admin.py file.
----------------------------------------------------------------------
next job is to actually go ahead and implement the view which we are going to go ahead and do
617. Form View & Template
--------------------
--
618. Handling Post Request
---
619. Adding Bootstrap
-----
620. Read Functionality
-----
621. Two Functionalities On Same Page
 in this field  add.html and index.html combine as index.html

622.Styling Part 1
623. Styling Part 2
624. Styling Part 3
displaying a shadow
creating style sheets
-----
625. Delete Functionality
-----
626. Add datetime
627. edit functionality
628. Introduction To Class Based & Generic Views
--------
What are class based views:-
view is nothing, but it's a callable which actually accepts a request and it returns back an appropriate response
views can actually be function based or class based.
 you can not only write views in terms of functions or Python functions, but you could also write views in terms of class as well.
  write in terms of class are actually called as a class based view.
  another subset of a class based view are called as generic views, and Django provides some built
  in class based views which are called as generic views or class based generic views.

  ---------
   focus is to go ahead and learn what are generic views and how to use them in our Django application.
   -------
what are generic views?
any Django application, we perform certain common tasks like listing out objects, displaying
want to develop, you always have to perform these certain generic tasks and therefore to handle these
particular tasks, Django provides us with certain views which you can use for these specific tasks.
 these specific views which Django provides, you are called as generic views.

So that means whenever you want to display a list of items, you don't have to write a full function based view

 Instead, you could simply write a class based generic view which is called as a list view.
 there are other generic views as well.  just like the list view, we have detailed view.You basically go ahead and display the details of a specific object.
 We have the create view to create a new object update view to update an object and delete view to delete
So depending upon what task you want to perform or what functionality you want to add, you can actually go ahead and use one of these views.

