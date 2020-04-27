# Docker App
* **Image Size** - 260MB
* Image name - SlotvalidateApp_image
* Conatiner name -SlotvalidateApp


## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **Django(https://www.django-rest-framework.org/)** - Django REST framework is a powerful and flexible toolkit for building Web APIs
* **Docker:18.09.9 (https://linuxize.com/post/how-to-install-and-use-docker-on-ubuntu-18-04/)** - Docker is a containerization technology
* Minor dependencies can be found in the requirements.txt file on the root folder.


### Steps for build and run Docker App
* Git clone this repo to your PC
* Build Docker image and Container
    > docker-compose up --build -d
* Check Docker Images & Container created
    > docker ps -a
    > docker images -a
* Run Docker App
    > docker start SlotvalidateApp
* Stop Docker App
    > docker stop SlotvalidateApp







