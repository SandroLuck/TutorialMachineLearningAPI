# General
This is the repository associated with the youtube tutorial at: TODO:
It is very simplistic and is meant as a guideline for implementing a Machine Learning API and not necessarily a good Machine Learning algorithm.
I put special emphasis on making this tutorial as short as possible

## To run:
cd to folder: `cd PATH/TO/MlApiTutorial`
run docker: `docker-compose up --build`
recommended: go in browser to http://localhost/docs (Assuming your docker hosts there else check `docker ps` it's on port 80)
you can test the api directly with GUI http://localhost/docs
or sent to http://localhost/will_survive

## For dev purposes
tests: `python -m main`
run server: `uvicorn main:app --reload`

## Trouble shoot
find ip: `docker ps`

## Files
'main.py' holds the API related code, put all in one file to make simpler.
'test.py' holds one test case to validate classifier is roughly working.
'Dockerfile' configures the server and installs dependencies. I used the Uvicorn/FastApi
'docker-compose.yml' not really needed. Simplifies execution on your side. I put restart:always incase you test edge cases (I did not handel them). 
'make_model.py' builds and selects a model. I did not validate them much, since this is more of a API tutorial.

## Test
I implemented a test just to integrate it.
In practice running them in Travis, Circelci before pulling from GitHub would be better.

## Deploy to a cloud
Check docker related deployment possibilities of your favorite cloud provider
