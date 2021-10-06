#!/bin/bash

#enable virtual environment

export FLASK_APP=app/main

export FLASK_RUN_PORT=8000

export FLASK_ENV=development

flask run