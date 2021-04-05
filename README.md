challenge Description

Write a Flask / FastAPI Web API that simulates the behavior of an audio file server while using a MongoDB / SQL database.

Requirements: You have one of three audio files which structures are defined below Audio file type can be one of the following:

1 – Song
2 – Podcast
3 – Audiobook

##Song file fields:

    ID – (mandatory, integer, unique)
    Name of the song – (mandatory, string, cannot be larger than 100 characters)
    Duration in number of seconds – (mandatory, integer, positive)
    Uploaded time – (mandatory, Datetime, cannot be in the past)

Podcast file fields:

    ID – (mandatory, integer, unique)
    Name of the podcast – (mandatory, string, cannot be larger than 100 characters)
    Duration in number of seconds – (mandatory, integer, positive)
    Uploaded time – (mandatory, Datetime, cannot be in the past)
    Host – (mandatory, string, cannot be larger than 100 characters)
    Participants – (optional, list of strings, each string cannot be larger than 100 characters, maximum of 10 participants possible)

##Audiobook file fields:

    ID – (mandatory, integer, unique)
    Title of the audiobook – (mandatory, string, cannot be larger than 100 characters)
    Author of the title (mandatory, string, cannot be larger than 100 characters)
    Narrator - (mandatory, string, cannot be larger than 100 characters)
    Duration in number of seconds – (mandatory, integer, positive)
    Uploaded time – (mandatory, Datetime, cannot be in the past)

API structuture is define in documentation folder. it is postman structure

Test challenge summary is define in documentation folder

##How to start

    Clone the repo from github git clone https://github.com/sahasrara62/filed_audio_file_server.git

    in terminal go to folder , cd filed_audio_file_server

    setup flask app

     a. export FLASK_APP=main.py
     b. export FLASK_ENV='developement'

    run flask server : flask run

    check if server is running at browser localhost:5000/ you will get , server is running
