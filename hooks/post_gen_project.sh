#!/bin/bash

pyenv local 2.7.12
pyenv virtualenv {{cookiecutter.project_slug}}
pyenv local {{cookiecutter.project_slug}}
pip install -r requirements.txt

# There's a starter workspace in the template but we don't want to track it from hereon out
echo .idea/workspace.xml >> .gitignore

git init .
git add -A
git commit -m "Initial commit."
hub create -p {{cookiecutter.github_repo}}
git push origin master
