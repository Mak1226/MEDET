# MEDET

The fully functional website can be seen on the following link:

https://medet124.pythonanywhere.com/

A website where you can search for various medicines, their uses , side effects etc, make your own profile, book mark medicine, have notes on medicine schedule, the list of doctors, list of medicines, and list of various details about the dieases etc.

this website also has a medicine recommendation system which recommends medicines based on the diseases entered in your profile,

and has news section from where people can get updates about the news related to health.

this website uses two API's
one for news(https://newsapi.org/) and other for the database of medicine(https://open.fda.gov/apis/)

This site uses HTML,CSS with some bootstrapping for frontend

And django in backend

for running backend server
first have python installed on your computer and then open the directory in which there is requirements.txt file
in the terminal run the following code

          python -m pip install -r requirements.txt
         
(note: make python3 as python alias, if you havent done already, if facing difficulty in doing that use pyhton3 instead of python everywhere)
          
Then go to the directory where manage.py file is located,
open the terminal run the following command to create a super user(admin user)

          python manage.py create superuser


after this it will ask for usernname and password enter anything you wish but just remeber it for accessing the admin page

PS- You can skip the step of making super user if you dont want to look at admin page

after this run the following commands to do the migrations

          python manage.py makemigrations
          python manage.py migrate
          
after doing this successfully,
run the following command

          python manage.py runserver
          
you will get the link of development server on the terminal itself  something like  http://127.0.0.1:8000/
copy the link run it in your browser and you can access the page
