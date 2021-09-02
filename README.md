# Docker App
* **Image Size** - 221MB
* Image name - slot_validator_image
* Conatiner name - slot_validator


## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[Django](https://www.django-rest-framework.org/)** - Django REST framework is a powerful and flexible toolkit for building Web APIs
* **[Docker:18.09.9](https://linuxize.com/post/how-to-install-and-use-docker-on-ubuntu-18-04/)** - Docker is a containerization technology
* Minor dependencies can be found in the requirements.txt file on the root folder.


### Steps to build and run Docker App
* Git clone this repo to your PC
* Install docker-compose and to run Docker commands as a non-root user without prepending sudo you need to add your user to the docker group
    > sudo usermod -aG docker $USER<br />
    > newgrp docker

* Build Docker image and Container
    > docker-compose up --build -d
* if not build then use
    > sudo docker-compose up --build -d
* Check created Docker Images & Container
    > docker ps -a <br />
    > docker images -a
* Run Docker App
    > docker start slot_validator
* Stop Docker App
    > docker stop slot_validator

* API endpoints for post request:

    > API for ID Validation request <br />
        > http://127.0.0.1:8000/api_1/IdValidation/ 
        <br />

    > API for Age Validation request <br />
        > http://127.0.0.1:8000/api_2/AgeValidation/


* Assumption
    > support_multiple and pick_first request attr both cannot be false simultaneously


This is my django first project







