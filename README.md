# SocialToCrowd

SocialToCrowd is a web application that allows people to request community help for
doing a project, but instead of asking for money you can ask for material
donations or volunteering work.

## How to run it:

1. Create a new virtualenv: mkvirtualenv -p /usr/bin/python2 socialtocrowd
1. Install requirements: pip install -r requirements.txt
1. Create the database:
    * install postgresql and postgis
    * Create a postgis database:
        *  $ sudo su - postgres
        *  $ createuser -P stc
        *  $ createdb -O stc stc
        *  $ psql stc
           * CREATE EXTENSION postgis;
           * CREATE EXTENSION postgis_topology;
    * python manage.py migrate
1. Run the application: python manage.py runserver


## Troubleshooting

Error: When I make ./manage.py migrate get the error: "UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3"

Solution: Execute: ./manage migrate project && ./manage.py migrate main && ./manage.py migrate
