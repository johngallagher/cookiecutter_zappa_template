#!/bin/bash

pyenv local 2.7.12
pyenv virtualenv {{cookiecutter.project_slug}}
pyenv local {{cookiecutter.project_slug}}
pip install -r requirements.txt

git init .
git add -A
git commit -m "Initial commit."
hub create -p {{cookiecutter.github_repo}}
git push origin master
