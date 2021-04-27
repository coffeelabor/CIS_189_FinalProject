# CIS_189_FinalProject


## Docker Terminal Commands

to build the project in the terminal:

> docker build -t python-final

to run the project from the terminal:

> docker run -p 8501:8501 python-final

if I Ctrl-C to end the run and then rerun it get a 'port is already allocated' error so I have to 'kill' it to get it to rerun.

This is where the problem is, when I update my code, it does not show up on the local version I have to 'kill' the container and rebuild it by doing the following in the terminal:

> docker ps

> docker kill <countainer-id>

After that I have to run the docker build and docker run again to see changes.

Is there a way to see live changes on my project, or even a command that will update the container so I can just do the run command again?