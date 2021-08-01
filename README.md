# MEDET
Design a website for people to login and get all the details of the medical conditions , medicines they are prescribed, when to eat the medicine. These entries will be provided by the user only which will be saved in the database and can be edited later on. the front home page will give info about other medicines which could be usefull for them. we want to have such a website as people tend to forget about names of medicines and stuff, so they can login and can tell all about their medical history just by looking at the website

This repos contains two directories
one for backend one for frontend work
The name of the frontend folder is frontend and backend  folder is backend

For now we will simply use html, css and js for frontend,

And django in backend

Dont do commits directly in the main branch...
if you wanna change anything then make a separate branch for it...
we will merge the branches after discussing among ourselves

we wont be linking frontend and backend for now...
we will link them later on after finishing up the the respective front end and backend part respectively

for running backend server
first have python and django installed on your local computer
Then go to the directory where manage.py file is located,
open the terminal run the following command to create a super user(admin user)

          python manage.py create superuser

(note: make python3 as python alias, if you havent done already, if facing difficulty in doing that use pyhton3 instead of python everywhere)
after this it will ask for usernname and password enter anything you wish but just remeber it for accessing the admin page

PS- You can skip the step of making super user if you dont want to look at admin page

after this run the following commands to do the migrations

          python manage.py makemigrations
          python manage.py migrate
          
after doing this successfully,
run the following command

          python manage.py runserver
          
ypou will get the link of development server on the terminal itself  something like  http://127.0.0.1:8000/
copy the link run it in your browser and you can access the page
