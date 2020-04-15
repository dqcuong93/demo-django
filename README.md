# demo-django
Demo of web app based on Django Python
To run this Web App, first setting up an local MySQL database 
for this app with the below information:
- NAME: 'storedb'
- USER: 'storeadmin'
- PASSWORD: 'P@ssw0rd'
- HOST: 'localhost' 
- PORT: 3306

Create an virtual environment in the app directory. 
For example: pipenv, virtualenv (or use your local environment, your choice).
Install all the packages in the requirements.txt file. 
After that, in your app directory run these line of command.

To show all migrations of the app: 
- python3 manage.py showmigrations

To make migrations note for the app: 
- python3 manage.py makemigrations

To migrate the first run information:
- python3 manage.py migrate

To create the superuser account:
- python3 manage.py createsuperuser

Finally, run the server:
- python3 manage.py runserver

(Authorized by Cuong Dao).
