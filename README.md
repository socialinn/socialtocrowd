# SocialCrowd

SocialCrowd is a web application to request to the comunity for help to
make a project, but instead of asking for money you can ask for material
donations or work to do.

## How to run it:

1. Create a new virtualenv: mkvirtualenv -p /usr/bin/python2 socialcrowd
1. Install requirements: pip install -r requirements.txt
1. Create the database:
    * python manage.py syncdb
    * python manage.py migrate
1. Run the application: python manage.py runserver
