# CIS_189_FinalProject


## Docker Terminal Commands

to build the project in the terminal:

> docker build -t python-final

to run the project from the terminal:

> docker run -p 8501:8501 -v <absolute path>:/driver.py python-final

docker run -p 8501:8501 -v 'C:\Users\Reed\Documents\6_DMACC\CIS_189_Final_Project\CIS_189_FinalProject\driver.py:/driver.py' python-final

to kill a container
> docker ps

> docker kill <countainer-id>
