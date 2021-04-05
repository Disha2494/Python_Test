# Problem Description

Write a Flask / FastAPI/ Django Web API Web API that simulates the behavior of an audio file server while using a MongoDB / SQL database.

Requirements: You have one of three audio files which structures are defined below Audio file type can be one of the following:

1 – Song
2 – Podcast
3 – Audiobook

## Song file fields:

    ID – (mandatory, integer, unique)
    Name of the song – (mandatory, string, cannot be larger than 100 characters)
    Duration in number of seconds – (mandatory, integer, positive)
    Uploaded time – (mandatory, Datetime, cannot be in the past)

## Podcast file fields:

    ID – (mandatory, integer, unique)
    Name of the podcast – (mandatory, string, cannot be larger than 100 characters)
    Duration in number of seconds – (mandatory, integer, positive)
    Uploaded time – (mandatory, Datetime, cannot be in the past)
    Host – (mandatory, string, cannot be larger than 100 characters)
    Participants – (optional, list of strings, each string cannot be larger than 100 characters, maximum of 10 participants possible)

## Audiobook file fields:

    ID – (mandatory, integer, unique)
    Title of the audiobook – (mandatory, string, cannot be larger than 100 characters)
    Author of the title (mandatory, string, cannot be larger than 100 characters)
    Narrator - (mandatory, string, cannot be larger than 100 characters)
    Duration in number of seconds – (mandatory, integer, positive)
    Uploaded time – (mandatory, Datetime, cannot be in the past)
    
# How to get started:
## To run the project following dependencies should be installed.
```
1: pip install pipenv
```
```
2: pipenv install django
```
```
3: pipenv install djangorestframework django-cors-headers
```
```
4: pipenv install django-mysql
```
### To activate the Virtual environment use:
```
pipenv shell
```
### For db migrations, use the following commands:
```
1. python manage.py makemigrations
2. python manage.py migrate
```

### To start the backend server use command:
```
python manage.py runserver
```
### To test the testcases run:
```
python manage.py test
```


