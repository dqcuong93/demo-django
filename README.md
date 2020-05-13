# demo-django

##Demo of a Web-App based on Django Python.

###LIST OF SERVICES/ LOCAL SERVER OF SERVICES
On MacOS install by brew
- elasticsearch-full       
- kafka                    
- mysql                    
- redis                    
- zookeeper
          
###IF YOU PULL THIS SOURCE USING GITHUB
To run this Web-App, first setting up an local MySQL database.
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

###IF YOU PULL THIS SOURCE USING DOCKER
First pull this resource by running this command: 
- docker pull dqcuong93/dockertest.

To run this Web-App, pull this file: https://github.com/dqcuong93/demo-django/blob/master/docker-compose.yml.

In your docker-compose.yml directory, run this command to create the super user account:
- docker-compose run web python3 manage.py createsuperuser.

Continue to create super user.

Then, Execute this command to start Web-App:
- docker-compose up 