#!/bin/bash

bin/setup

# There's a starter workspace in the template but we don't want to track from now on
echo .idea/workspace.xml >> .gitignore

git init .
git add -A
git commit -m "Initial commit."
hub create -p {{cookiecutter.github_repo}}
git push origin master
