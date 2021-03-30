# spacex\_api

Project Backend Space-x

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

**License:** MIT

Documentation
-------------

The official documentation of this project is located in
**docs/\_build/index.html**, but before looking for it, you\'ll have to
do some steps.

1. Download [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
2.  Execute in terminal `docker-compose -f local.yml build` and `docker-compose -f local.yml up docs`. This will create the `_build` directory with all the web structure for the docs.
3.  Download and install `ritwickdey.liveserver` extension for VS code. If you have another editor, search for another live server.
4.  Open the `docs/\_build/index.html` file in VS Code. Press \"Go Live\", and automatically the browser will open the docs in web format.
5. Enjoy my docs made with love... 😎
